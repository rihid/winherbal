from django.db import models
from django.conf import settings
from django.urls import reverse

class ArCategory(models.Model):
    name = models.CharField(max_length=15, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta: 
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name

class Article(models.Model):
    kategori = models.ForeignKey(ArCategory, related_name='article', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pengupload')
    judul = models.CharField(max_length=150)
    penulis = models.CharField(max_length=15, default='admin')
    body = models.TextField(blank=True)
    gambar = models.ImageField(upload_to='blog/', default='images/default.png')
    slug = models.SlugField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    
    class Meta:
        verbose_name_plural = 'Articles'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[self.slug])
    
    def __str__(self):
        return self.judul

    
