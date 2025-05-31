from django.http import HttpResponse
from django.template import loader

from .models import Produto


def index(request):
    latest_question_list = Produto.objects.all()
    template = loader.get_template("produto/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))