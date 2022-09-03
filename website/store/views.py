from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger #Untuk Pagination
from .models import Category, Product
from blog.models import Article


def home(request):
    products_grid = Product.products.all()
    articles_grid = Article.objects.all()

    # Pagination Product
    page = request.GET.get('page', 1)
    paginator = Paginator(products_grid, 3)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    # Pagination Artikel
    page_ar = request.GET.get('page', 1)
    paginator_ar = Paginator(articles_grid, 3)
    try:
        articles = paginator_ar.page(page_ar)
    except PageNotAnInteger:
        articles = paginator_ar.page(1)
    except EmptyPage:
        articles = paginator_ar.page(paginator_ar.num_pages)

    return render(request, 'store/index.html', {
        'products': products,
        'articles': articles,
        })


def product_all(request):
    products_grid = Product.products.all()
    
    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(products_grid, 6)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'store/product.html', {'products': products})

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.products.filter(category=category)
    return render(request, 'store/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/single.html', {'product': product})
