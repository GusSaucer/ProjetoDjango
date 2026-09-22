from django.shortcuts import render


def home_view(request):
    return render(request,'home.html')

def produtos_view(request):
    lista_produtos = [
            {'nome': "Monitor", "preco": 700.00, "estoque": 5},
            {'nome': "PC Desktop", "preco": 5050.00, "estoque": 2},
            {'nome': "SmartWach", "preco": 200.00, "estoque": 7},
            {'nome': "Cadeira Gamer", "preco": 900.00, "estoque": 1},
            {'nome': "Teclado Mecânico", "preco": 400.00, "estoque": 11},
    ]

    context = {'produtos': lista_produtos}
    
    return render(request,'produtos.html', context)

def perfil_view(request):
    context = {'nome_usuario': 'Gustavo' , 'cargo': 'Instrutor' , 'setor': 'TI'}

    return render(request,'perfil.html', context)

def status_view(request):
    context = {'admin': False ,'id_servidor': '127.0.0.1' , 'status_sistema': '200 OK - Online'}

    return render(request,'status.html', context)