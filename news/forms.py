from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    """Форма комментариев"""
    class Meta:
        model = Comment
        fields = ("text",)
        widgets = {
            "text": forms.Textarea(attrs={"rows": 15, "cols": 5, "class": "text-text"})
        }
