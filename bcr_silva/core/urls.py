from django.urls import path

from bcr_silva.core import views

app_name = "core"
urlpatterns = [
    path("", views.home, name="home"),
]