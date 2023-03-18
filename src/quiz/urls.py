from django.contrib import admin
from django.urls import include, path
from quiz.views import bitcoin, normalize_email

urlpatterns = [
    path("bitcoin/", bitcoin, name="bitcoin"),
    path("normalize_email/", normalize_email, name='normalize_email'),
]




