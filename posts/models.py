from django.db import models
from ckeditor.fields import RichTextField

from authors.models import Author


class Rubric(models.Model):
    pass


class Post(models.Model):
    slug = models.SlugField(max_length=255, verbose_name='Семантический URL')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    body = RichTextField()
    created_at = models.DateTimeField(verbose_name='Создано', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Редактировано', auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='posts', verbose_name='Автор', null=True)
    is_active = models.BooleanField(verbose_name='Отображать на сайте', default=True)
    meta_description = models.TextField(verbose_name='МЕТА Описание')
    meta_keywords = models.TextField(verbose_name='МЕТА Ключевые слова')
    preview_image = models.ImageField(verbose_name='Превью изображение', upload_to='uploads/posts/preview/%y/%m/%d/')
    rubric = models.ForeignKey(Rubric, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-created_at', ]
