from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Ticket(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    text = models.TextField("Сообщение")
    created = models.DateTimeField("Дата сообщения", auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.user, self.created)

    def get_absolute_url(self):
        return reverse('ticket-list')

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщение"
        ordering = ["-created"]
