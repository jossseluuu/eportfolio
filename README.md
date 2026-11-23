# eportfolio

Personal e-portfolio of **José Luis López López**, Computer Engineering student at the
University of Granada. Bilingual (English / Spanish).

**Live site:** https://jossseluuu.github.io/eportfolio/

## How it works

The site is a **Django** project. GitHub Pages can only serve static files, so Django is used
as a static site generator:

```
main/content.py  ──►  Django views + templates  ──►  manage.py build  ──►  dist/ (HTML)  ──►  GitHub Pages
```

- **Development:** `python manage.py runserver` serves the real Django app.
- **Publishing:** on every push to `main`, GitHub Actions runs the tests, renders every page
  with `python manage.py build` and deploys `dist/` to GitHub Pages.

No database, no cookies, no analytics and no third-party scripts (strict Content Security Policy).

## Project structure

```
eportfolio/                     Django settings and root URLs
main/
  content.py                    All the content, in English and Spanish (edit this to update the site)
  views.py, urls.py             /  ·  /projects/<slug>/  ·  /es/  ·  /es/projects/<slug>/
  templates/main/               base, home, project_detail, 404
  static/                       css, js, images, CV and portfolio PDFs
  management/commands/build.py  Static export for GitHub Pages
  tests.py
.github/workflows/pages.yml     Build and deploy
```

## Run locally

```bash
python -m venv venv
venv\Scripts\activate          # Windows  (source venv/bin/activate on Linux/macOS)
pip install -r requirements.txt

python manage.py runserver     # http://127.0.0.1:8000/  and  /es/
python manage.py test
python manage.py build         # writes the static site to dist/
```

To preview the static build exactly as GitHub Pages will serve it:

```bash
python manage.py build --base-path /
python -m http.server 8000 --directory dist
```

## Updating content

1. Edit `main/content.py`. Every translatable text is `T("English", "Español")`.
2. Add images to `main/static/img/` and reference them from the project's `images` list.
3. Commit and push to `main`. The site redeploys automatically.

## Deployment setup (once)

In the repository on GitHub: **Settings → Pages → Build and deployment → Source: GitHub Actions**.

## Tech

Python 3.12 · Django 5.2 · HTML · CSS (no framework) · vanilla JavaScript · GitHub Actions · GitHub Pages
