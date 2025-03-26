from django.contrib import admin

from .models import Produto, Pedido, PedidoItem

# Register your models here.

admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(PedidoItem)