from django.urls import path, include
from .views import PostView, perfil_usuario, PostSucessoView, pagina_inicial

urlpatterns = [
    path('conta/', include('django.contrib.auth.urls')),
    path('', perfil_usuario, name="perfil_usuario"),
    path('post/', PostView.as_view(), name="post"),
    path('sucesso/', PostSucessoView.as_view(), name="post_sucesso"),
    path('inicio/', pagina_inicial, name="index"),
    #path('publicacao/')
]
