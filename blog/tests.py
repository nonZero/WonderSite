from django.core.urlresolvers import reverse
from django.test import TestCase
from blog.models import Post


class BlogTestCase(TestCase):
    def test_create_posts(self):
        p = Post()
        p.title = "Hello world"
        p.content = "blah blah blah"
        p.save()

        self.assertEqual(Post.objects.count(), 1)

    def test_homepage(self):
        p = Post()
        p.title = "Hello world"
        p.content = "blah blah blah"
        p.save()

        url = reverse('home')
        resp = self.client.get(url)
        self.assertContains(resp, "Hello world")

    def test_contents(self):

        p = Post()
        p.title = "Hello world"
        p.content = "blah blah blah"
        p.save()

        p = Post()
        p.title = "Daily Summary"
        p.content = "blah blah blah"
        p.save()

        p = Post()
        p.title = "Trip to USA"
        p.content = "blah blah blah"
        p.save()

        url = reverse('contents')
        resp = self.client.get(url)
        self.assertContains(resp, "<li>Hello world</li>")
        self.assertContains(resp, "<li>Hello world</li>")
        self.assertContains(resp, "<li>Trip to USA</li>")

