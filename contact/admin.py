from django.contrib import admin

from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    """Тикеты"""
    list_display = ("user", "created")
