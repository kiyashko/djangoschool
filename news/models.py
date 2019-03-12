from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """Модель категорий статей"""
    name = models.CharField("Имя", max_length=100)
    slug = models.SlugField("url", max_length=100)
    template = models.CharField("Шаблон", max_length=500, default="news/post-list.html")
    posts_amount = models.IntegerField("Количество новостей", default="5")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория статей"
        verbose_name_plural = "Категории статей"


class Tag(models.Model):
    """Модель тегов"""
    name = models.CharField("Имя", max_length=100)
    slug = models.SlugField("url", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Post(models.Model):
    """Статьи"""
    author = models.ForeignKey(
        User,
        verbose_name="Автор",
        on_delete=models.CASCADE
    )
    title = models.CharField("Заголовок", max_length=100)
    headline = models.CharField("Подзаголовок", max_length=300)
    main_image = models.ImageField(upload_to = 'post_images/', blank=True, null=True)
    text = models.TextField("Текст")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    publicated = models.DateTimeField("Дата публикации", auto_now_add=False)
    edited = models.DateTimeField("Дата редактирования", auto_now_add=False)
    add_post = models.BooleanField("Опубликовать?", default=True)
    displayregister = models.BooleanField("Для всех?", default=True)
    template = models.CharField("Шаблон", max_length=500, default="news/post-detail.html")
    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.SET_NULL,
        null=True
    )
    tags = models.ManyToManyField(Tag, verbose_name="Теги")
    slug = models.SlugField("url", max_length=100, null=True)

    def __str__(self):
        return self.title

    def get_comments(self):
        return Comment.objects.filter(post_id=self.id)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["-created"]


class Comment(models.Model):
    """Модель комментариев к статье"""
    post = models.ForeignKey(
        Post,
        verbose_name="Статья",
        on_delete=models.CASCADE
    )
    text = models.TextField("Комментарий")
    moderation = models.BooleanField("Разрешено к публикации", default=False)
    created = models.DateTimeField("Дата написания", auto_now_add=True)

    def __str__(self):
        return "{}".format(self.post.title)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["-created"]
