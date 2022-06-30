from django.urls import path, include
from .views import PostView, perfil_usuario, pagina_inicial, PostSucessoView, ComentarioView, publicacao

urlpatterns = [
    path('conta/', include('django.contrib.auth.urls')),
    path('perfil/', perfil_usuario, name="perfil_usuario"),    
    path('inicio/', pagina_inicial, name="index"),
    path('post/', PostView.as_view(), name="post"),
    path('sucesso/', PostSucessoView.as_view(), name="post_sucesso"),
    path('publicacao/<int:id_publi>', publicacao, name="publicacao"),
    path('comentario/<int:id_publi>', ComentarioView.as_view(), name="comentario"),
]
