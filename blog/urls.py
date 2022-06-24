from django.contrib import admin
from django.urls import path, include
from microblog.views import PostView, perfil_usuario, PostSucessoView, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('microblog.urls')),
    path('', include('django.contrib.auth.urls')),
    path('perfil/', perfil_usuario, name="perfil_usuario"),
    path('post/', PostView.as_view(), name="post"),
    path('sucesso/', PostSucessoView.as_view(), name="post_sucesso"),
    path('inicio/', index, name="index")
]
