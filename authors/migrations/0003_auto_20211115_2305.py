# Generated by Django 3.2.9 on 2021-11-15 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authors', '0002_auto_20211115_2254'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='author',
            name='password',
        ),
        migrations.AddField(
            model_name='author',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='auth.user', verbose_name='Пользователь'),
            preserve_default=False,
        ),
    ]
