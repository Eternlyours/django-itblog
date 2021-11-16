from django.contrib import admin

from posts.models import Post, Rubric


class PostAdmin(admin.ModelAdmin):
    fields = ('created_at', 'updated_at', 'author', 'rubric', 'is_active', 'slug', 'title' , 'preview_image', 'thumb_image', 'body', 'meta_description', 'meta_keywords', )
    readonly_fields = ('created_at', 'updated_at', 'slug', 'thumb_image', )
    list_display = ('title', 'rubric', 'thumb_image', 'is_active', )
    list_display_links = ('title', )
    list_editable = ('is_active', )
    

class RubricAdmin(admin.ModelAdmin):
    fields = ('slug', 'name', 'description', 'is_active', 'meta_description', 'meta_keywords' ,)
    readonly_fields = ('slug', )
    list_display = ('slug', 'name', 'is_active', )
    list_display_links = ('slug', 'name', )
    list_editable = ('is_active', )


admin.site.register(Post, PostAdmin)
admin.site.register(Rubric, RubricAdmin)