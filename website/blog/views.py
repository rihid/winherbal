from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger #Untuk Pagination
from .models import Article, ArCategory

def categories(request):
    return {
        'categories' : ArCategory.objects.all()
    }

def all_article(request):
    articles_grid = Article.objects.all()
    
    # Pagination Artikel
    page_ar = request.GET.get('page', 1)
    paginator_ar = Paginator(articles_grid, 6)
    try:
        articles = paginator_ar.page(page_ar)
    except PageNotAnInteger:
        articles = paginator_ar.page(1)
    except EmptyPage:
        articles = paginator_ar.page(paginator_ar.num_pages)

    return render(request, 'blog/blog.html', {'articles' : articles})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug,)
    return render(request, 'blog/single-news.html', {'article' : article})

