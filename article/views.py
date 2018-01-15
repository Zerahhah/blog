from django.shortcuts import render,redirect
from django.http import  HttpResponse,Http404
from django.template.loader import get_template
from .models import Article
from datetime import datetime

# Create your views here.


def homepage(request):
    template = get_template('homepage.html')
    html = template.render()
    return HttpResponse(html)


def article(request,num):
    id = int(num)
    template = get_template('base.html')
    try:
        articles = Article.objects.get(id=id)
        if articles != None:
            now = datetime.now()
            html = template.render(locals())
            return HttpResponse(html)
    except:
        raise Http404