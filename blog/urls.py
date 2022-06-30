from django.contrib import admin
from django.urls import path, include
from microblog.views import usuario, followers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('microblog.urls')),
    path('<str:user>/', usuario, name="usuario"),
    path('<str:user>/followers', followers, name="followers"),
]
