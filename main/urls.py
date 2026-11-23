from django.urls import path

from . import views

urlpatterns = [
    # English (default)
    path("", views.home, {"lang": "en"}, name="home_en"),
    path("projects/<slug:slug>/", views.project, {"lang": "en"}, name="project_en"),
    # Spanish
    path("es/", views.home, {"lang": "es"}, name="home_es"),
    path("es/projects/<slug:slug>/", views.project, {"lang": "es"}, name="project_es"),
    # Rendered to 404.html by the static build
    path("404.html", views.not_found, name="not_found"),
]
