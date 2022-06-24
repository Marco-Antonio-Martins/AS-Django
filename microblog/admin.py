from django.contrib import admin

from .models import Comentario, Pessoa, Post


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ("usuario", "nome",)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("autor", "descricao_curta", "data",)

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("autor", "descricao_curta_post", "descricao_curta_comentario", "data")
