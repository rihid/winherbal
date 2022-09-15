from django.conf import settings
from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from django.core.exceptions import ValidationError


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(max_length=15, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

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
            # "Gambar yang anda upload lebih besar dari %(size)skB."
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


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = HTMLField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='images/default.png', validators=[ImageValidator(size=200000,)], help_text=_("Ukuran Maksimal Gambar 2 MB"))
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.title
