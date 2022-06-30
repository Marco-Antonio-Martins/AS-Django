from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .forms import PostForm, ComentarioForm
from .models import Pessoa, Post, Comentario
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
        return reverse('post') #alterar para post_sucesso


class PostSucessoView(TemplateView):

    template_name = 'microblog/post_sucesso.html'


def perfil_usuario(request): #Mostra o perfil do usuário logado

    usuario = request.user
          
    if usuario.is_authenticated:

        usuario = Pessoa.objects.get(usuario = request.user)      
    
    return render(request, 'microblog/perfil_usuario.html', {'usuario' : usuario})


def usuario(request, user): #Mostra o perfil do usuário solicitado

    try:
        usuario = request.user
        seguidora = False
        pessoa = Pessoa.objects.get(usuario__username__contains=user)
        posts = pessoa.post_set.all()
        if usuario.is_authenticated:            
            usuario = Pessoa.objects.get(usuario=usuario)   

            for s in usuario.get_seguidores():
                seguidor = Pessoa.objects.get(usuario = s)
                if seguidor == pessoa:
                    if seguidor != usuario:
                        seguidora = True

    except Pessoa.DoesNotExist:

        raise Http404('Nome de Usuário não encontrado')

    return render(request, 'microblog/perfil.html', {'usuario' : usuario,'pessoa' : pessoa, 'posts' : posts, 'seguidora' : seguidora})

def pagina_inicial(request): #Mostra a página inicial do usuário logado

    usuario = request.user
    posts = []
          
    if usuario.is_authenticated:

        usuario = Pessoa.objects.get(usuario = request.user)  
    
        for s in usuario.get_seguidores():
            seguidor = Pessoa.objects.get(usuario = s)
            if seguidor != usuario:
                for p in seguidor.post_set.all():
                    if len(posts) < 30:
                        posts.append(p)
    
    return render(request, 'microblog/pagina_inicial.html', {'usuario' : usuario, 'posts' : posts})

def followers(request, user):
    if request.method == 'POST':
        try:
            usuario = request.user
            is_follow = request.POST['is_follow']
            
            if usuario.is_authenticated:            
                usuario = Pessoa.objects.get(usuario_id=request.user.id)   
                pessoa = Pessoa.objects.get(usuario__username=user)

                if is_follow == 'follow':
                    usuario.seguindo.add(pessoa.usuario)
                if is_follow == 'unfollow':
                    usuario.seguindo.remove(pessoa.usuario.id)
                    

        except Pessoa.DoesNotExist:

            raise Http404('Nome de Usuário não encontrado')

    return HttpResponseRedirect(reverse('usuario', args=[user]))

def publicacao(request, id_publi):

    usuario = request.user
    if usuario.is_authenticated:
        usuario = Pessoa.objects.get(usuario = request.user)
    publicacao = Post.objects.get(pk=id_publi)
    pessoa = Pessoa.objects.get(usuario=publicacao.autor.usuario)
    comentarios = publicacao.comentario_set.all()
    return render (request, 'microblog/publicacao.html', {'usuario' : usuario, 'publicacao' : publicacao, 'comentarios' : comentarios, 'pessoa' : pessoa})
 
class ComentarioView(FormView):

    template_name = 'microblog/comentario.html'
    form_class = ComentarioForm

    def get(self, request, **kwargs):

        usuario = self.request.user
        if usuario.is_authenticated:
            usuario = Pessoa.objects.get(usuario = usuario)
        publicacao = Post.objects.get(pk=kwargs['id_publi'])
        return render (request, self.template_name, {'usuario' : usuario, 'publicacao' : publicacao, 'form' : self.form_class })
    
    def form_valid(self, form):  

        usuario = self.request.user

        if usuario.is_authenticated:

            usuario = Pessoa.objects.get(usuario = usuario)            
            dados = form.clean()
            publicacao = Post.objects.get(pk=dados['id_publi'])
            comentario = Comentario(autor=usuario, post=publicacao, conteudo=dados['comentario'])
            comentario.save()
            return super().form_valid(form)
          

    def get_success_url(self):
        id = str(self.kwargs['id_publi'])
        return reverse('publicacao', args=[id])