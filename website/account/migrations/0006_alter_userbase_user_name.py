# Generated by Django 3.2 on 2022-09-11 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20220903_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbase',
            name='user_name',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]