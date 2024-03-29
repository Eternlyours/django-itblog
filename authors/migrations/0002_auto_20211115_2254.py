# Generated by Django 3.2.9 on 2021-11-15 17:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='avatar',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='uploads/authors/%y/%m/%d/', verbose_name='Аватар'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='biography',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='Краткая биография автора'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='author',
            name='password',
            field=models.CharField(default=0, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
