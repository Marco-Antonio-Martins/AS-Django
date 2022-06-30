from django import forms

class PostForm(forms.Form):
  mensagem = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder' : 'O que você está pensando?'}), max_length=200)

class ComentarioForm(forms.Form):
  comentario = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder' : 'Adicione o comentário da publicação aqui:'}), max_length=200)
  id_publi = forms.IntegerField(widget=forms.HiddenInput())