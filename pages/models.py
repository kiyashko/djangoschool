from django.db import models

class Page(models.Model):
    """Модель страниц"""
    title = models.CharField("Заголовок", max_length=500)
    content = models.TextField("Текст")
    created = models.DateTimeField("Дата", auto_now_add=True)
    template = models.CharField("Шаблон", max_length=500, default="pages/index.html")
    slug = models.SlugField(
        "URL",
        max_length=500,
        unique=True,
        default='',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return self.title

class ContactForm(models.Model):
    """Модель формы обратной связи"""
    first_name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=30)
    email = models.EmailField("E-Mail", max_length=70)
    text = models.TextField("Сообщение")
    created = models.DateTimeField("Дата сообщения", auto_now_add=True)

    def __str__(self):
        return "{}".format(self.email)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ["-created"]
