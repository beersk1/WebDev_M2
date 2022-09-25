from dataclasses import field
from .models import Task
from django import forms


class Taskforms(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'