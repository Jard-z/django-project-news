from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *


def index(request):
    news = News.objects.all()
    context = {'news': news,
               'title': 'Список новостей',
               }
    return render(request, 'news/home.html', context)


def get_categories(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {'news': news,
               'category': category,
               }
    return render(request, 'news/category.html', context)


def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    context = {'news_item': news_item}
    return render(request, 'news/view_news.html', context)


def add_news(request):
    if request.method == 'POST':
        pass
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})
