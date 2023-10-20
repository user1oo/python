from django.contrib import admin
from crud_blog_web.models import Article

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass