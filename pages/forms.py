from django import forms

from .models import ContactForm

class ContactForm(forms.ModelForm):
    """Форма обратной связи"""
    class Meta:
        model = ContactForm
        fields = ['first_name', 'last_name', 'email', 'text']
