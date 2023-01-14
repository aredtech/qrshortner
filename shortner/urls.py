from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("<str:url>/", views.ShortUrlView.as_view(), name="redirect_url"),
    path("shorten/manage/", views.ShortUrlManageView.as_view(), name="short_url"),
    path("shorten/manage/<str:url>/", views.ShortUrlManageView.as_view(), name="short_url-detail"),
]
