from django.contrib import admin

from .models import Post, Category, Tag, Comment

from mptt.admin import MPTTModelAdmin

admin.site.site_title = "Django Course"
admin.site.site_header = "Django Course"

@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    """Категории"""
    prepopulated_fields = {'slug': ('name',)}
    mptt_level_indent = 20

class CommentAdmin(admin.TabularInline):
    """Комментарии в статьях"""
    model = Comment
    extra = 1
    template = 'admin/news/news.html'
    list_display = ("id", "post", "moderation")
    list_editable = ("moderation",)

class PostAdmin(admin.ModelAdmin):
    """Статьи"""
    list_display = ("id", "title", "created")
    list_display_links = ("title",)
    search_fields = ("title",)
    list_filter = ("created", "category")
    filter_vertical = ("tags",)
    show_full_result_count = False
    inlines = [CommentAdmin]
    prepopulated_fields = {"slug": ("title",)}

class CommentsAdmin(admin.ModelAdmin):
    """Комментарии в админке"""
    list_display = ("id", "post", "created")
    list_display_links = ("id", "post")
    list_filter = ("created",)

admin.site.unregister(Category)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentsAdmin)
