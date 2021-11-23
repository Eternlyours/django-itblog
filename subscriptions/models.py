from django.db import models
from posts.models import Rubric

from readers.models import Reader


class Subscription(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, related_name='subscriptions', verbose_name='Подписчик')
    rubrics = models.ManyToManyField(Rubric, related_name='subscriptions', verbose_name='Рубрики')
    is_active = models.BooleanField(verbose_name='Активность', default=True)
    created_at = models.DateTimeField(verbose_name='Дата подписки', auto_now_add=True)

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

