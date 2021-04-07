from django.contrib import admin

from .models import New

@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'publicationDate')
    list_filter = ('user', 'publicationDate')
    search_fields = ("title__startswith", )
