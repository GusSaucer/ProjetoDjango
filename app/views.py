import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout  # <-- Adicionado logout
from .forms import CadastroComEmailForm  # Importando o novo formulário que criamos

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
    # Se o usuário já estiver logado, não precisa ver a tela de cadastro
    if request.user.is_authenticated:
        return redirect('produtos')

    if request.method == 'POST':
        # Usamos o novo formulário que exige o e-mail
        form = CadastroComEmailForm(request.POST)
        
        if form.is_valid():
            # 1. Salva o usuário no banco de dados
            user = form.save()
            
            # --- INTEGRAÇÃO EMAILJS ---
            emailjs_url = 'https://api.emailjs.com/api/v1.0/email/send'
            
            # Monta o pacote de dados para a API
            payload = {
                'service_id': 'service_3pwl0dv',     # Ex: service_xxxxx
                'template_id': 'template_fbnp5dd',   # Ex: template_xxxxx
                'user_id': 'u8BgNyrmh9VGjmfgf',        # Ex: abcdef123456
                'accessToken': 'RwnlvDMOPlT9f5xwpqPcH',   # A chave secreta do painel
                'template_params': {
                    'nome_usuario': user.username,
                    'email_destino': user.email     # Agora temos a garantia de que o e-mail existe!
                }
            }
            
            # Tenta fazer o disparo sem travar o sistema do aluno caso a internet caia
            try:
                resposta = requests.post(emailjs_url, json=payload)
                if resposta.status_code != 200:
                    print(f"Erro EmailJS: {resposta.text}")
            except Exception as e:
                print(f"Erro de conexão com EmailJS: {e}")
            # --------------------------

            # 2. Faz o login automático e redireciona para a loja
            login(request, user)
            return redirect('produtos')
    else:
        # Se for GET, exibe o formulário vazio
        form = CadastroComEmailForm()

    return render(request, 'cadastro.html', {'form': form})

def detalhes_produto_view(request, id):
    # Busca o produto cuja PK seja igual ao ID da URL
    # get_object_or_404 retorna erro 404 se não encontrar
    produto_banco = get_object_or_404(Produto, id=id)

    return render(request,'detalhes_produto.html',{'produto': produto_banco})