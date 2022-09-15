from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product_all, name='product_all'),
    path('tentang/', views.about, name='tentang'),
    path('kontak/', views.kontak, name='kontak'),
    path('product/<slug:slug>', views.product_detail, name='product_detail'),
    path('product/detail/<slug:category_slug>/', views.category_list, name='category_list'),
]
