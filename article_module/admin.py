from django.contrib import admin
from django.http import HttpRequest

from . import models
from .models import Article


# Register your models here.
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'parent', 'is_active']
    list_editable = ['url_title', 'is_active', 'parent']


class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'slug', 'is_active', 'auther'
    ]
    list_editable = [
        'is_active'
    ]

    def save_model(self, request: HttpRequest, obj: Article, form, change):
        if not change:
            obj.auther = request.user
        return super().save_model(request, obj, form, change)


class article_comment_Admin(admin.ModelAdmin):
    list_display = [
        'user', 'create_date', 'parent',
    ]


admin.site.register(models.ArticleCategory, ArticleCategoryAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.article_comments, article_comment_Admin)
