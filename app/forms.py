from django import forms
from .models import Produto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','preco','estoque','imagem']

class CadastroComEmailForm(UserCreationForm):
    # Adicionamos o campo de e-mail e o tornamos obrigatório
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        # Definimos exatamente quais campos vão aparecer no HTML
        fields = ("username", "email")