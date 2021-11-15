from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='author', verbose_name='Пользователь')
    biography = models.TextField(verbose_name='Краткая биография автора')
    avatar = models.ImageField(verbose_name='Аватар', upload_to='uploads/authors/%y/%m/%d/')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
