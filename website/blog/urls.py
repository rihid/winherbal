from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_article, name='all_article'),
    path('<slug:slug>', views.article_detail, name='article_detail'),
    
]
