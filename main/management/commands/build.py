"""
Render the whole site to static HTML for GitHub Pages.

    python manage.py build                       # -> dist/, served under /eportfolio/
    python manage.py build --base-path /         # for a user site or a custom domain

Each page is requested through Django's test client, so the output is exactly
what ``runserver`` shows. Static files are copied next to the HTML.
"""

import shutil
from datetime import date
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.test import Client, override_settings
from django.urls import clear_script_prefix, reverse, set_script_prefix

from main.content import LANGS, project_slugs


class Command(BaseCommand):
    help = "Render the site to static HTML (for GitHub Pages)."

    def add_arguments(self, parser):
        parser.add_argument("--output", default=str(settings.BASE_DIR / "dist"))
        parser.add_argument("--base-path", default="/eportfolio/",
                            help="URL path the site is served under (default: /eportfolio/).")

    def handle(self, *args, **opts):
        out = Path(opts["output"]).resolve()
        base = "/" + opts["base_path"].strip("/") + "/"
        base = "/" if base == "//" else base

        if out == settings.BASE_DIR.resolve() or settings.BASE_DIR.resolve().is_relative_to(out):
            raise CommandError(f"Refusing to wipe {out}")
        if out.exists():
            shutil.rmtree(out)
        out.mkdir(parents=True)

        with override_settings(
            FORCE_SCRIPT_NAME=base.rstrip("/") or None,
            STATIC_URL=f"{base}static/",
            DEBUG=False,
        ):
            set_script_prefix(base)
            try:
                pages = self._render_pages(out, base)
            finally:
                clear_script_prefix()

        self._copy_static(out)
        self._write_extras(out, pages)
        self.stdout.write(self.style.SUCCESS(f"Built {len(pages)} pages into {out}"))

    # ------------------------------------------------------------------

    def _routes(self):
        routes = []
        for lang in LANGS:
            routes.append(reverse(f"home_{lang}"))
            for slug in project_slugs():
                routes.append(reverse(f"project_{lang}", kwargs={"slug": slug}))
        return routes

    def _render_pages(self, out, base):
        client = Client(SERVER_NAME="localhost")
        written = []
        routes = self._routes() + [reverse("not_found")]
        for url in routes:
            path_info = url[len(base) - 1:] if base != "/" else url
            response = client.get(path_info)
            if response.status_code != 200:
                raise CommandError(f"{path_info} returned {response.status_code}")
            rel = path_info.lstrip("/")
            target = out / rel / "index.html" if rel == "" or rel.endswith("/") else out / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(response.content)
            if rel != "404.html":
                written.append(rel)
            self.stdout.write(f"  {url}")
        return written

    def _copy_static(self, out):
        src = settings.BASE_DIR / "main" / "static"
        shutil.copytree(src, out / "static")

    def _write_extras(self, out, pages):
        # GitHub Pages: serve files as-is, without Jekyll processing.
        (out / ".nojekyll").write_text("")

        site = settings.SITE_URL.rstrip("/")
        today = date.today().isoformat()
        entries = "\n".join(
            f"  <url><loc>{site}/{p}</loc><lastmod>{today}</lastmod></url>" for p in pages
        )
        (out / "sitemap.xml").write_text(
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{entries}\n</urlset>\n",
            encoding="utf-8",
        )
