from django.urls import path
from . import views

app_name = "feed"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:article_id>/", views.detail, name="detail"),
    # path("/", views.about, name="about"),
]
