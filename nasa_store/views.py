from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.template import loader

from .models import Produto, PedidoItem, Pedido


def index(request):
    latest_question_list = Produto.objects.all()
    template = loader.get_template("produto/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detalhes(request, id):
    latest_question_list = Produto.objects.get(pk=id)
    template = loader.get_template("produto/details.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def carrinho(request):
    latest_question_list = PedidoItem.objects.all()
    template = loader.get_template("carrinho/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def adicionar_carrinho(request, id):
    pedido = Pedido.objects.create(nome_cliente="The Beatles")
    pedido.save()

    pedido_item = PedidoItem(produto_id=id, pedido_id=pedido.id, quantidade=1, preco_un=10.99)
    pedido_item.save()

    return HttpResponseRedirect("/carrinho/")

def remover_carrinho(request, id):
    PedidoItem.objects.filter(id=id).delete()

    return HttpResponseRedirect("/carrinho/")