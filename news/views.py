from datetime import datetime

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Post, Category, Comment
from .forms import CommentForm


class PostList(ListView):
    """Список статей"""
    context_object_name = 'posts'

    def get_queryset(self):
        if self.kwargs.get('category') is not None:
            post_list = Post.objects.filter(
                category__slug=self.kwargs.get('category'),
                published=True,
                published_date__lte=datetime.now(),
            )
            if self.request.user.is_authenticated:
                posts = post_list
            else:
                posts = post_list.filter(status=False)

            if posts.exists():
                self.paginate_by = posts.first().category.pagination
                self.template_name = posts.first().category.template
        else:
            posts = Post.objects.all()
            self.paginate_by = 5
            self.template_name = 'news/post-list.html'
        return posts


class PostDetail(DetailView):
    """Вывод полной статьи"""
    model = Post
    template_name = 'news/post-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

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
