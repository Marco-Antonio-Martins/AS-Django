from django import forms

class PostForm(forms.Form):
  mensagem = forms.CharField(widget=forms.Textarea)