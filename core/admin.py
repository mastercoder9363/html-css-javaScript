from django.contrib import admin
from .models import *

@admin.register(TopPost)
class ArticleTopPost(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name', 'abo')