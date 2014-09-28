import random

from django.shortcuts import render, get_object_or_404

from blog.models import Post


def home(request):
    return render(request, "blog/home.html", {
        'lucky': random.randint(1, 10),
        'x': Post.objects.count(),
        'object_list': Post.objects.all(),
    })


def single_post(request, pk):
    return render(request, "blog/post.html", {
        #'object': Post.objects.get(pk=int(pk)),
        'object': get_object_or_404(Post, pk=int(pk)),
    })