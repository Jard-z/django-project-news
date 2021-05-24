from django.shortcuts import render
from .models import *


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {'news': news,
               'title': 'Список новостей',
               'categories': categories,
               }
    return render(request, 'news/home.html', context)


def get_categories(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {'news': news,
               'categories': categories,
               'category': category,
               }
    return render(request, 'news/category.html', context)
