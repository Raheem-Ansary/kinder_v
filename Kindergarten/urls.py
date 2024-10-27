# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("articles/", views.kindergarten_articles, name="kindergarten_articles"),
]
