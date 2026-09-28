from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout  # <-- Adicionado logout

def home_view(request):
    return render(request, 'home.html')

def produtos_view(request):
    lista_produtos = Produto.objects.all()
    form = ProdutoForm()

    if request.method == 'POST':
        if 'produto_id' in request.POST:
            produto = get_object_or_404(Produto, id=request.POST.get('produto_id'))
            form = ProdutoForm(request.POST, instance=produto)
        else:
            form = ProdutoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('produtos')

    context = {
        'produtos': lista_produtos,
        'form': form,
    }
    return render(request, 'produtos.html', context)

def perfil_view(request):
    # Protege a rota caso o usuário não esteja autenticado
    if not request.user.is_authenticated:
        return redirect('login')

    context = {
        'nome_usuario': request.user.username,
        'email': request.user.email,
        'cargo': 'Instrutor',
        'setor': 'TI'
    }
    return render(request, 'perfil.html', context)


def status_view(request):
    context = {'admin': False, 'id_servidor': '127.0.0.1', 'status_sistema': '200 OK - Online'}
    return render(request, 'status.html', context)

def cadastro_view(request):
    if request.user.is_authenticated:
        return redirect('produtos')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('produtos')
    else:
        form = UserCreationForm()

    return render(request, 'cadastro.html', {'form': form})