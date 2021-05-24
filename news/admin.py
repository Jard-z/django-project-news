from django.contrib import admin
from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'create_date', 'update_date', 'is_published')
    list_editable = ('is_published',)
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content')
    list_filter = ('category', 'is_published')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category)
