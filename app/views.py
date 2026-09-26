from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm

def home_view(request):
    return render(request, 'home.html')

def produtos_view(request):
    lista_produtos = Produto.objects.all()
    form = ProdutoForm()

    if request.method == 'POST':
        # Se veio 'produto_id', é uma EDIÇÃO (UPDATE)
        if 'produto_id' in request.POST:
            produto = get_object_or_404(Produto, id=request.POST.get('produto_id'))
            form = ProdutoForm(request.POST, instance=produto)
        # Se NÃO veio, é um NOVO produto (CREATE)
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
    context = {'nome_usuario': 'Gustavo' , 'cargo': 'Instrutor' , 'setor': 'TI'}

    return render(request,'perfil.html', context)

def status_view(request):
    context = {'admin': False ,'id_servidor': '127.0.0.1' , 'status_sistema': '200 OK - Online'}

    return render(request,'status.html', context)
