from django import template
from news.models import *
from django.db.models import *
from django.core.cache import cache

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories():
    # cache menu sidebar
    # categories = cache.get('categories')
    # if not categories:
    #     categories = Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0,)
    #     cache.set('categories', categories)

    categories = Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0, )
    return {"categories": categories, }
