from django.contrib import admin

from readers.models import Reader


class ReaderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Reader, ReaderAdmin)
