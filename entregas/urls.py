
from django.urls import path
from .views import lista_entregas

urlpatterns = [
    path("", lista_entregas, name="lista_entregas"),
]
