from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    # path("/", views.detail, name="detail"),
    # path("/", views.about, name="about"),
]