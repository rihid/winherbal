# Generated by Django 3.1.4 on 2022-08-31 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbase',
            name='address_line_1',
        ),
        migrations.RemoveField(
            model_name='userbase',
            name='address_line_2',
        ),
        migrations.AddField(
            model_name='userbase',
            name='alamat',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
