from django.shortcuts import render


def home_view(request):
    return render(request,'home.html')

def produtos_view(request):
    context = {'nome': "Monitor", "preco": 700.00, "estoque": 3}
    
    return render(request,'produtos.html', context)

def perfil_view(request):
    context = {'nome_usuario': 'Gustavo' , 'cargo': 'Instrutor' , 'setor': 'TI'}

    return render(request,'perfil.html', context)

def status_view(request):
    context = {'admin': True ,'id_servidor': '127.0.0.1' , 'status_sistema': '200 OK - Online'}

    return render(request,'status.html', context)