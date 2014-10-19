from django.contrib import admin
from blog import models


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'is_published',
        'published_at',
        'author',
        'category',
    ]
    list_filter = [
        'is_published',
        'priority',
        'category',
    ]
    search_fields = [
        'title',
        'author',
        'content',
    ]


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Category)
admin.site.register(models.Tag)
