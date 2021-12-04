from django.db import models


class PostQuerySet(models.QuerySet):
    def tags(self):
        return self.prefetch_related('tags')

    def only_active(self):
        return self.filter(is_active=True)