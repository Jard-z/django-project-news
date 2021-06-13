from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView
from django.core.mail import send_mail

from .forms import ContactForm, NewsForm
from .models import *
from .utils import MyMixin


def send_message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['zazimko1995@gmail.com', ]
            mail = send_mail(subject, message, email_from, recipient_list, fail_silently=True)
            if mail:
                messages.success(request, 'Отправлено!')
                return redirect('send_mail')
            else:
                messages.error(request, 'Ошибка отправки!')
    else:
        form = ContactForm()
    return render(request, 'news/send_mail.html', {'form': form})


class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'news/home.html'
    context_object_name = 'news'
    mixin_prop = 'hello world'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(HomeNews, self).get_context_data(**kwargs)
        context['title'] = 'Главная'
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.select_related('category').filter(is_published=True).select_related('category')


class NewsCategory(ListView):
    model = News
    template_name = 'news/home.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(NewsCategory, self).get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewNews(DetailView):
    model = News
    template_name = 'news/view_news.html'


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    login_url = '/admin/'

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
