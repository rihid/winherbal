from django.contrib import admin
from .models import Article, ArCategory

@admin.register(ArCategory)
class ArCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(Article)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['judul', 'author', 'created', 'updated']
    prepopulated_fields = {'slug' : ('judul',)}