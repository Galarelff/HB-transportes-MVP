from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_entregas, name="lista_entregas"),
    path(
        "entrega/<str:numero>/atualizar-status/",
        views.atualizar_status,
        name="atualizar_status",
    ),
]