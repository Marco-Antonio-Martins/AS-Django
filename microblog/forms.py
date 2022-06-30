from django import forms

class PostForm(forms.Form):
  mensagem = forms.CharField(widget=forms.Textarea, max_length=200)

class ComentarioForm(forms.Form):
  comentario = forms.CharField(widget=forms.Textarea, max_length=200)
  id_publi = forms.IntegerField(widget=forms.HiddenInput())