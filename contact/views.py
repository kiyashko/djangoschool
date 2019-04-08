from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Ticket
from .forms import TicketForm

class TicketList(ListView):
    """Список сообщения пользователя"""
    template_name = "contact/ticket-list.html"
    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)

class TicketCreate(CreateView):
    """Создание тикета"""
    model = Ticket
    form_class = TicketForm
    template_name = "contact/ticket-form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_valid(form)

class TicketUpdate(UpdateView):
    """Редактирование тикета"""
    model = Ticket
    form_class = TicketForm
    template_name = "contact/ticket-form.html"

class TicketDelete(DeleteView):
    """Удаление тикета"""
    model = Ticket
    template_name = "contact/ticket-delete.html"
    success_url = reverse_lazy('ticket-list')
