from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import truncatechars


class Pessoa(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário', unique=True)
    nome = models.CharField(max_length=150)
    seguindo = models.ManyToManyField(User, blank=True, related_name='seguindo') #releted_name é pra n usar _set.all

    def get_seguidores(self):
        return self.seguindo.all()
    
    def __str__(self):
        return self.nome

    def arroba(self):
        return self.usuario.get_username()

class Post(models.Model):

    autor = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Autor")
    conteudo = models.CharField(max_length=200)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-data",)
    
    def __str__(self):
        return self.conteudo

    #SilvioEdit // Função que retorna a descrição curta de 100 caracteres do conteudo
    @property
    def descricao_curta(self):
        return truncatechars(self.conteudo, 100) 
    # Exemplo de uso no admin.py
                                                                

class Comentario(models.Model):
    
    autor = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Autor")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Post")
    conteudo = models.CharField(max_length=200)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("data",)

    def __str__(self):
        return self.conteudo

    #SilvioEdit // Aqui foram precisas duas funções por conta das duas variaveis serem max_length=200
    @property
    def descricao_curta_post(self):
        return truncatechars(self.post, 100) 
    @property
    def descricao_curta_comentario(self):
        return truncatechars(self.conteudo, 100)

        