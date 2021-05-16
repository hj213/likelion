from django import forms
from django.forms import fields, models
from .models import blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = ['title', 'writer', 'body', 'image']