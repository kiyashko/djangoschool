from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    """Модель категорий статей"""
    name = models.CharField("Имя", max_length=100)
    slug = models.SlugField("url", max_length=100)
    pagination = models.PositiveIntegerField('Кол. для пагинации', default=5)
    template = models.CharField(
        'Используемый шаблон',
        max_length=100,
        blank=False,
        default='news/post-list.html'
    )

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
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    title = models.CharField("Заголовок", max_length=100)
    subtitle = models.CharField('Подзаголовок', max_length=100, blank=False, default='')
    mini_text = models.TextField("Краткое содержание", max_length=1000, default='')
    text = models.TextField("Текст")
    image = models.ImageField('Главное изображение', upload_to='post/', blank=True)
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    template = models.CharField(
        'Используемый шаблон',
        max_length=100,
        blank=False,
        default='news/post-detail.html'
    )
    edit_date = models.DateTimeField(
        "Дата редактирования",
        default=timezone.now,
        blank=True,
        null=True
    )
    published_date = models.DateTimeField(
        "Дата публикации",
        default=timezone.now,
        blank=True,
        null=True)
    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.SET_NULL,
        null=True
    )
    tags = models.ManyToManyField(Tag, verbose_name="Теги")
    published = models.BooleanField("Опубликовать?", default=True)
    status = models.BooleanField("Для зарегистрированных", default=False)
    slug = models.SlugField("url", max_length=100)
    viewed = models.PositiveIntegerField("Просмотров", default=0)

    def __str__(self):
        return self.title

    def get_comments(self):
        return Comment.objects.filter(post_id=self.id)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"category": self.category.slug, "slug": self.slug})

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
