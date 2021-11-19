from django.db import models
from django.template.defaultfilters import slugify
from unidecode import unidecode


class Tag(models.Model):
    slug = models.SlugField(verbose_name='Семантический URL', max_length=50)
    word = models.CharField(verbose_name='Слово', max_length=50)
    created_at = models.DateTimeField(
        verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.word

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.word))
        return super().save(*args, **kwargs)
