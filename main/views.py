from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.urls import get_script_prefix, reverse

from .content import get_context


def _absolute(url):
    """Turn a reversed URL (which includes the script prefix) into a public URL."""
    prefix = get_script_prefix()
    if url.startswith(prefix):
        url = url[len(prefix):]
    return f"{settings.SITE_URL.rstrip('/')}/{url}"


def _base_context(lang, page, **kwargs):
    ctx = get_context(lang)
    other = "es" if lang == "en" else "en"
    urls = {code: reverse(f"{page}_{code}", kwargs=kwargs) for code in ("en", "es")}
    ctx.update(
        lang=lang,
        other_lang=other,
        home_url=reverse(f"home_{lang}"),
        alt_url=urls[other],
        canonical_url=_absolute(urls[lang]),
        en_abs_url=_absolute(urls["en"]),
        es_abs_url=_absolute(urls["es"]),
    )
    return ctx


def home(request, lang):
    return render(request, "main/home.html", _base_context(lang, "home"))


def project(request, slug, lang):
    ctx = _base_context(lang, "project", slug=slug)
    projects = ctx["featured_projects"]
    index = next((i for i, p in enumerate(projects) if p["slug"] == slug), None)
    if index is None:
        raise Http404("Unknown project")
    ctx["project"] = projects[index]
    ctx["next_project"] = projects[(index + 1) % len(projects)]
    return render(request, "main/project_detail.html", ctx)


def not_found(request):
    ctx = _base_context("en", "home")
    ctx["es_ui"] = get_context("es")["ui"]
    ctx["es_home_url"] = reverse("home_es")
    return render(request, "main/404.html", ctx)
