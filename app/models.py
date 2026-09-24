from django.db import models

# tipo string -> CharField(max_length=*)
# tipo inteiro -> IntegerField()
# tipo decimal -> FloatField()
# tipo booleano -> BooleanField()

class Produtos(models.Model): # o certo é PRODUTO , no singular
    nome = models.CharField(max_length=200)
    preco = models.FloatField()
    estoque = models.IntegerField()
    imagem = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.nome