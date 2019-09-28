from django import forms

from .models import TimeTable


class TimeTableForm(forms.ModelForm):
    class Meta:
        model = TimeTable
        fields = ("title", "description", "is_published")
