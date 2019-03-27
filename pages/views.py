from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.http import HttpResponse
from .forms import ContactForm

from .models import Page


class PageView(View):
    """Вывод страницы"""
    def get(self, request, page=None):
        if page is None:
            one_page = get_object_or_404(Page, slug__isnull=True)
        else:
            one_page = get_object_or_404(Page, slug=page)
        return render(request, one_page.template, {"page": one_page})

    """Сообщение пользователя"""
    def post(self, request, page):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("news")
        else:
            return redirect("news")
