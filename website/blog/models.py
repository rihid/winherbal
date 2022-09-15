from django.db import models
from django.conf import settings
from django.urls import reverse
from tinymce.models import HTMLField
from django.core.exceptions import ValidationError

class ArCategory(models.Model):
    name = models.CharField(max_length=15, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta: 
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name

try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping

from django.utils.translation import ugettext_lazy as _
from django.utils.deconstruct import deconstructible


@deconstructible
class ImageValidator(object):
    messages = {
        "size": _(
            # "File is larger than > %(size)skB."
            "Gambar yang anda unggah lebih besar dari 2 MB."
        )
    }

    def __init__(self, size=None, messages=None):
        self.size = size
        if messages is not None and isinstance(messages, Mapping):
            self.messages = messages

    def __call__(self, value):
        # _get_image_dimensions is a method of ImageFile
        # https://docs.djangoproject.com/en/1.11/_modules/django/core/files/images/
        if self.size is not None and value.size > self.size:
            raise ValidationError(
                self.messages['size'],
                code='invalid_size',
                params={
                    'size': float(self.size)/1024,
                    'value': value,
                }
            )

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            self.size == other.size
        )

class Article(models.Model):
    kategori = models.ForeignKey(ArCategory, related_name='article', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pengupload')
    judul = models.CharField(max_length=150)
    penulis = models.CharField(max_length=15, default='admin')
    body = HTMLField(blank=True)
    gambar = models.ImageField(
        upload_to='blog/', default='images/default.png', validators=[ImageValidator(size=2000000,)], help_text=_("Ukuran Maksimal Gambar 2 MB"))
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

    
