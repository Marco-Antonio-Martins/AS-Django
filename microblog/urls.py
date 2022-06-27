from django.urls import path, include
from .views import PostView, perfil_usuario, PostSucessoView, index

urlpatterns = [
    path('conta/', include('django.contrib.auth.urls')),
    path('perfil/', perfil_usuario, name="perfil_usuario"),
    path('post/', PostView.as_view(), name="post"),
    path('sucesso/', PostSucessoView.as_view(), name="post_sucesso"),
    path('inicio/', index, name="index"),
]
