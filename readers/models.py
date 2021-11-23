from django.db import models


class Reader(models.Model):
    email = models.EmailField(verbose_name='Электронная почта', unique=True)
    name = models.CharField(verbose_name='Имя', max_length=100)
    is_active = models.BooleanField(verbose_name='Активность', default=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'


