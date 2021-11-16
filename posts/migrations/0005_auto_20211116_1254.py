# Generated by Django 3.2.9 on 2021-11-16 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20211116_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='Семантический URL'),
        ),
        migrations.AlterField(
            model_name='rubric',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название рубрики'),
        ),
    ]