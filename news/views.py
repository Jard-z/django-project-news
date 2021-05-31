from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView


from .models import *
from .forms import *


class HomeNews(ListView):
    model = News
    template_name = 'news/home.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super(HomeNews, self).get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsCategory(ListView):
    model = News
    template_name = 'news/home.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super(NewsCategory, self).get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


class ViewNews(DetailView):
    model = News
    template_name = 'news/view_news.html'


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'

# def index(request):
#    news = News.objects.all()
#    context = {'news': news,
#               'title': 'Список новостей',
#               }
#    return render(request, 'news/home.html', context)


#def get_categories(request, category_id):
#    news = News.objects.filter(category_id=category_id)
#    category = Category.objects.get(pk=category_id)
#    context = {'news': news,
#               'category': category,
#               }
#    return render(request, 'news/category.html', context)


#def view_news(request, news_id):
#    news_item = get_object_or_404(News, pk=news_id)
#    context = {'news_item': news_item}
#    return render(request, 'news/view_news.html', context)


#def add_news(request):
#    if request.method == 'POST':
#        form = NewsForm(request.POST)
#        if form.is_valid():
#            # news = News.objects.create(**form.cleaned_data)
#            news = form.save()
#            return redirect(news)
#    else:
#        form = NewsForm()
#    return render(request, 'news/add_news.html', {'form': form})
