from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _


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


class Tag(models.Model):
    slug = models.CharField(max_length=200, null=True, blank=True, unique=True)
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title



class Category(models.Model):
    slug = models.CharField(max_length=200, null=True, blank=True, unique=True)
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    title = models.CharField(_("Title"), max_length=200)
    content = models.TextField(_("Content"))
    published_at = models.DateTimeField(_("Published at"), auto_now_add=True)
    author = models.CharField(max_length=100, null=True, blank=True)

    priority = models.PositiveIntegerField(choices=Priority.choices,
                                           default=Priority.NORMAL)

    category = models.ForeignKey(Category, null=True, blank=True,
                                 related_name='posts')

    tags = models.ManyToManyField(Tag, blank=True)

    poster = models.ImageField(upload_to="posters", null=True, blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", args=(self.pk,))


    class Meta:
        verbose_name = _("Blog Post")
        verbose_name_plural = _("Blog posts")


class FavouritePost(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            ('post', 'user'),
        )
