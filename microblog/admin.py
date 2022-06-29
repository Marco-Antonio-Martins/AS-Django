from django.contrib import admin

from .models import Comentario, Pessoa, Post


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    pass
