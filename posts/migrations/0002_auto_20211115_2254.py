# Generated by Django 3.2.9 on 2021-11-15 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='meta_description',
            field=models.TextField(default=0, verbose_name='МЕТА Описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='meta_keywords',
            field=models.TextField(default=0, verbose_name='МЕТА Ключевые слова'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='preview_image',
            field=models.ImageField(default=0, upload_to='uploads/posts/preview/%y/%m/%d/', verbose_name='Превью изображение'),
            preserve_default=False,
        ),
    ]
