from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Produto: {self.nome} - {self.preco}'

class Pedido(models.Model):
    nome_cliente = models.CharField(max_length=200)
    nome_vendedor = models.CharField(max_length=200)
    pago = models.BooleanField(default=False)

    def __str__(self):
        return f'Pedido: #{self.id} - {self.nome_cliente} - {self.nome_vendedor} - Pago? {self.pago}'

class PedidoItem(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_un = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Item do pedido: #{self.pedido.id} - {self.produto.nome} - {self.quantidade} x {self.preco_un}'