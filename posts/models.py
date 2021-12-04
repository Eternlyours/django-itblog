from datetime import datetime

from authors.models import Author
from ckeditor.fields import RichTextField
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone
from posts.manager import PostManager
from tags.models import Tag
from unidecode import unidecode


class Rubric(models.Model):
    slug = models.SlugField(max_length=255, verbose_name='Семантический URL')
    name = models.CharField(
        max_length=255, verbose_name='Название рубрики', unique=True)
    description = models.TextField(verbose_name='Описание рубрики')
    is_active = models.BooleanField(
        verbose_name='Отображать на сайте', default=True)
    meta_description = models.TextField(verbose_name='МЕТА Описание')
    meta_keywords = models.TextField(verbose_name='МЕТА Ключевые слова')

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        return super().save(*args, **kwargs)

    def count_posts(self):
        return self.posts.count()


class Post(models.Model):
    slug = models.SlugField(
        max_length=255, verbose_name='Семантический URL', unique=True)
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    body = RichTextField(verbose_name='Контент')
    created_at = models.DateTimeField(
        verbose_name='Создано')
    updated_at = models.DateTimeField(
        verbose_name='Редактировано', auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,
                               related_name='posts', verbose_name='Автор', null=True)
    is_active = models.BooleanField(
        verbose_name='Отображать на сайте', default=True)
    meta_description = models.TextField(verbose_name='МЕТА Описание')
    meta_keywords = models.TextField(verbose_name='МЕТА Ключевые слова')
    preview_image = models.ImageField(
        verbose_name='Превью изображение', upload_to='uploads/posts/preview/%y/%m/%d/')
    rubric = models.ForeignKey(Rubric, on_delete=models.SET_NULL,
                               null=True, related_name='posts', verbose_name='Рубрика')
    tags = models.ManyToManyField(
        Tag, related_name='posts', verbose_name='Теги', )

    objects = PostManager()

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-created_at', ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.localtime(timezone.now())
        self.slug = slugify(
            f'{unidecode(self.title)}{datetime.strftime(self.created_at, "-%Y-%m-%d-%H%M%S")}')
        return super().save(*args, **kwargs)

    def thumb_image(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src=%s width="150" height="150" style="object-fit:cover;" />' % (self.preview_image.url))

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})

    def get_next_post(self):
        post = Post.objects.filter(
            is_active=True, created_at__gt=self.created_at).order_by('created_at').values('slug', 'title', 'preview_image').first()
        if post is None:
            post = Post.objects.order_by('created_at').values('slug', 'title', 'preview_image').first()
        return post

    def get_prev_post(self):
        post = Post.objects.filter(
            is_active=True, created_at__lt=self.created_at).order_by('created_at').values('slug', 'title', 'preview_image').first()
        if post is None:
            post = Post.objects.order_by('-created_at').values('slug', 'title', 'preview_image').first()
        return post