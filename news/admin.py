from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('id', 'title', 'category', 'create_date', 'update_date', 'is_published', 'get_photo')
    list_editable = ('is_published',)
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content')
    list_filter = ('category', 'is_published')
    fields = ('title', 'category', 'content', 'photo', 'get_photo', 'create_date', 'update_date', 'is_published')
    readonly_fields = ('get_photo', 'create_date', 'update_date')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100">')
        else:
            return '-'

    get_photo.short_description = 'Фото'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category)
admin.site.site_title = 'title'
admin.site.site_header = 'header'
