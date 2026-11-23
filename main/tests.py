from django.test import SimpleTestCase
from django.urls import reverse

from .content import FEATURED_PROJECTS, LANGS, T, project_slugs


class PagesTest(SimpleTestCase):
    def test_home_pages(self):
        for lang in LANGS:
            response = self.client.get(reverse(f"home_{lang}"))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, f'<html lang="{lang}">')

    def test_project_pages(self):
        for lang in LANGS:
            for slug in project_slugs():
                response = self.client.get(reverse(f"project_{lang}", kwargs={"slug": slug}))
                self.assertEqual(response.status_code, 200)

    def test_unknown_project_is_404(self):
        response = self.client.get("/projects/does-not-exist/")
        self.assertEqual(response.status_code, 404)

    def test_phone_number_is_not_published(self):
        for url in ("/", "/es/"):
            html = self.client.get(url).content.decode()
            self.assertNotIn("659", html)


class ContentTest(SimpleTestCase):
    def test_every_bilingual_string_has_both_languages(self):
        def walk(node, path="content"):
            if isinstance(node, T):
                for lang in LANGS:
                    self.assertTrue(node.get(lang), f"Missing {lang} text at {path}")
            elif isinstance(node, dict):
                for k, v in node.items():
                    walk(v, f"{path}.{k}")
            elif isinstance(node, (list, tuple)):
                for i, v in enumerate(node):
                    walk(v, f"{path}[{i}]")

        walk(FEATURED_PROJECTS)
