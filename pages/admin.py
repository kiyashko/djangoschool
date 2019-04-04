from django.contrib import admin

from .models import Page, ContactForm

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    """Админ страниц"""
    list_display = ("title", "id")
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(ContactForm)
