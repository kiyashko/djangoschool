from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic.base import View

from .models import Post, Category
from .forms import CommentForm


class PostList(View):
    """Список статей"""
    def get(self, request, slug=None):
        if slug is not None:
            posts = get_list_or_404(Post, category__slug=slug)
        else:
            posts = Post.objects.all()
        return render(request, 'news/post-list.html', {"posts": posts})


class PostDetail(View):
    """Вывод полной статьи"""
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        return render(request, 'news/post-detail.html', {"post": post})

    """Добавление комментариев"""
    def post(self, request, slug):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = Post.objects.get(slug=slug)
            form.save()
            return redirect("news")
        else:
            return HttpResponse(status=400)
