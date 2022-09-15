# Generated by Django 3.1 on 2022-09-14 23:37

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20220915_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='gambar',
            field=models.ImageField(default='images/default.png', help_text='Ukuran Maksimal Gambar 2 MB', upload_to='blog/', validators=[blog.models.ImageValidator(size=2000000)]),
        ),
    ]
