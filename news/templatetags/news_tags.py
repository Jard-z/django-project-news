from django import template
from news.models import Category


reqister = template.Library()


@reqister.simple_tag()
def get_categories():
    return Category.objects.all()