from django.urls import path

from . import views

app_name = "inicio"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("tema/<slug:slug>/", views.tema_detalle, name="tema"),
]