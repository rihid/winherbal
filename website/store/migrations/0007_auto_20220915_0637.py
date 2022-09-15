# Generated by Django 3.1 on 2022-09-14 23:37

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20220915_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='images/default.png', help_text='Ukuran Maksimal Gambar 2 MB', upload_to='images/', validators=[store.models.ImageValidator(size=2000000)]),
        ),
    ]