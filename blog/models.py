from django.conf import settings
from django.db import models


class Priority(object):
    VERY_HIGH = 5
    HIGH = 4
    NORMAL = 3
    LOW = 2
    VERY_LOW = 1

    choices = (
        (VERY_HIGH, "Very high"),
        (HIGH, "High"),
        (NORMAL, "Normal"),
        (LOW, "Low"),
        (VERY_LOW, "Very low"),
    )


class Category(models.Model):
    slug = models.CharField(max_length=200, null=True, blank=True, unique=True)
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, null=True, blank=True)

    priority = models.PositiveIntegerField(choices=Priority.choices,
                                           default=Priority.NORMAL)

    category = models.ForeignKey(Category, null=True, blank=True,
                                 related_name='posts')

    def __unicode__(self):
        return self.title
