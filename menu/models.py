from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from mptt.models import MPTTModel, TreeForeignKey

class Menu(models.Model):
    """Меню"""
    name = models.CharField("Имя", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

class MenuItem(MPTTModel):
    """Меню"""
    name = models.CharField("Имя", max_length=150)
    parent = TreeForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )

    menu = models.ForeignKey(Menu, verbose_name="Меню", on_delete=models.CASCADE)
    url = models.CharField("Url на внешний ресурс", max_length=500, blank=True, null=True)

    limit = models.Q(app_label='pages', model='page') | \
            models.Q(app_label='news', model='post') | \
            models.Q(app_label='news', model='сategory')

    content_type = models.ForeignKey(
        ContentType,
        verbose_name='Ссылка на',
        limit_choices_to=limit,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    object_id = models.PositiveIntegerField(verbose_name='Id записи', default=1, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пункт Меню"
        verbose_name_plural = "Пункты Меню"
