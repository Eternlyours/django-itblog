from django.contrib import admin

from posts.models import Post, Rubric


class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('is_active', 'slug', ('created_at', 'updated_at', ), ('rubric', 'author',), ('preview_image', 'thumb_image'), ),
        }),
        ('Теги', {
            'classes': ('collapse', ),
            'fields': ('tags', )
        }),
        ('Контент', {
            'fields': ('title', 'body', )
        }),
        ('META', {
            'fields': ('meta_description', 'meta_keywords', )
        }),
    )
    filter_horizontal = ('tags', )
    readonly_fields = ('created_at', 'updated_at', 'slug', 'thumb_image', )
    list_display = ('title', 'rubric', 'thumb_image', 'is_active', )
    list_display_links = ('title', )
    list_editable = ('is_active', )
    list_filter = ('is_active', 'tags', 'rubric', )
    date_hierarchy = 'created_at'
    search_fields = ('title', 'body', 'tags__word', 'rubric__name', )
    save_on_top = True
    list_select_related = True

    class Media:
        css = {
             'all': ('admin/css/table.css',)
        }


class RubricAdmin(admin.ModelAdmin):
    fields = ('slug', 'name', 'description', 'is_active',
              'meta_description', 'meta_keywords',)
    readonly_fields = ('slug', )
    list_display = ('slug', 'name', 'is_active', )
    list_display_links = ('slug', 'name', )
    list_editable = ('is_active', )


admin.site.register(Post, PostAdmin)
admin.site.register(Rubric, RubricAdmin)
