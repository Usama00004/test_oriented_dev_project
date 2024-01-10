from django import forms
from .models import Author


class MyModelForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio',]
