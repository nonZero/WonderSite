from django.contrib import admin
from blog import models


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'published_at',
    ]


admin.site.register(models.Post, PostAdmin)
