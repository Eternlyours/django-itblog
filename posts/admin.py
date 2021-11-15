from django.contrib import admin

from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    fields = ('created_at', 'updated_at', 'author', 'is_active', 'slug', 'title' , 'preview_image', 'body', 'meta_description', 'meta_keywords', )
    readonly_fields = ('created_at', 'updated_at', 'slug', )
    radio_fields = {'author': admin.VERTICAL}

admin.site.register(Post, PostAdmin)
