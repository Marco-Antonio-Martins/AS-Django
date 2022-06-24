from django.urls import path

from .views import usuario

urlpatterns = [
    path('<str:user>/', usuario, name="usuario"),
]
