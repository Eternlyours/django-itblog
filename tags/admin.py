from django.contrib import admin

from tags.models import Tag


class TagAdmin(admin.ModelAdmin):
    fields = ('created_at', 'slug', 'word', )
    readonly_fields = ('created_at', 'slug', )


admin.site.register(Tag, TagAdmin)
