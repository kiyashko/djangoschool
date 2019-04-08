from django import forms

from .models import Ticket

class TicketForm(forms.ModelForm):
    """Форма тикетов"""
    class Meta:
        model = Ticket
        fields = ['text', ]
