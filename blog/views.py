import random
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse

from django.shortcuts import render, get_object_or_404, redirect
from blog.forms import MyForm, PostForm

from blog.models import Post, Category


def home(request):
    return render(request, "blog/home.html", {
        'lucky': random.randint(1, 10),
        'x': Post.objects.count(),
        'object_list': Post.objects.filter(is_published=True).order_by(
            '-published_at')[:5],
    })


def category(request, slug):
    c = get_object_or_404(Category, slug=slug)
    return render(request, "blog/home.html", {
        'category': c,
        'object_list': c.posts.filter(is_published=True).order_by(
            '-published_at')[:5],
    })


def contents(request):
    return render(request, "blog/contents.html", {
        'object_list': Post.objects.all(),
    })


def single_post(request, pk):
    return render(request, "blog/post.html", {
        # 'object': Post.objects.get(pk=int(pk)),
        'object': get_object_or_404(Post, pk=int(pk)),
    })


@login_required
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            post = form.save()
            return redirect(reverse('home'))
    else:
        form = PostForm()
    return render(request, "blog/feedback.html", {
        'form': form,
    })

def feedback(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            assert False, form.cleaned_data
    else:
        form = MyForm()
    return render(request, "blog/feedback.html", {
        'form': form,
    })

