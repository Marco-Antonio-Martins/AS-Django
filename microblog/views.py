from django.http import Http404
from django.shortcuts import render
from .forms import PostForm
from .models import Pessoa, Post
from django.views.generic import FormView, TemplateView
from django.urls import reverse


class PostView(FormView):

    template_name = 'microblog/post.html'
    form_class = PostForm
    
    def form_valid(self, form):

        usuario = self.request.user    

        if usuario.is_authenticated:

            usuario = Pessoa.objects.get(usuario = self.request.user)
            dados = form.clean()
            mensagem = Post(autor=usuario, conteudo=dados['mensagem'])
            mensagem.save()
            return super().form_valid(form)
          

    def get_success_url(self):
        return reverse('post_sucesso')


class PostSucessoView(TemplateView):

    template_name = 'microblog/post_sucesso.html'


def perfil_usuario(request): #Mostra o perfil do usuário logado

    usuario = request.user
          
    if usuario.is_authenticated:

        usuario = Pessoa.objects.get(usuario = request.user)      
    
    return render(request, 'microblog/perfil_usuario.html', {'usuario' : usuario})


def usuario(request, user): #Mostra o perfil do usuário solicitado

    try:
        
        pessoa = Pessoa.objects.get(usuario__username__contains=user)

    except Pessoa.DoesNotExist:

        raise Http404('Nome de Usuário não encontrado')

    posts = pessoa.post_set.all()

    return render(request, 'microblog/perfil.html', {'pessoa' : pessoa, 'posts' : posts})

def index(request): #Mostra o perfil do usuário logado

    usuario = request.user
          
    if usuario.is_authenticated:

        usuario = Pessoa.objects.get(usuario = request.user)      
    
    return render(request, 'microblog/index.html', {'usuario' : usuario})