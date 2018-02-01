from django.shortcuts import render,redirect
from django.http import  HttpResponse,Http404
from django.template.loader import get_template
from .models import Article , CountView
from datetime import datetime

# Create your views here.


def welcome(request):
    template = get_template('welcome.html')
    html = template.render()
    return  HttpResponse(html)

def homepage(request):
    template = get_template('homepage.html')
    html = template.render()
    return HttpResponse(html)


def article(request,num):
    id_num = int(num)
    template = get_template('base.html')
    '''+1总浏览'''
    today = datetime.now()
    try:
        query = CountView.objects.get_queryset()
        query = query.filter(the_date__year=today.year,the_date__month=today.month)
        res = query.get(the_date__day=today.day)
        if res != None:
            res.count_views += 1
            res.save()
    except:
        CountView.objects.create(the_date=today)

    '''单个博客浏览'''
    try:
        articles = Article.objects.get(id=id_num)
        if articles != None:
            articles.view_count += 1
            articles.save()
            html = template.render(locals())
            return HttpResponse(html)
    except:
        raise Http404