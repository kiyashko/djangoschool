from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.base import View

from .models import Post, Category


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
