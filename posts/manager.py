from django.db import models

from posts.querysets import PostQuerySet


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def posts(self):
        return self.get_queryset().tags()