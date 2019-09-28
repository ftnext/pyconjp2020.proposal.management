from django import forms

from .models import TimeTable, TimeTableColumn, TimeTableRow


class TimeTableForm(forms.ModelForm):
    class Meta:
        model = TimeTable
        fields = ("title", "description", "is_published")


class TimeTableColumnForm(forms.ModelForm):
    class Meta:
        model = TimeTableColumn
        fields = ("name",)


class TimeTableRowForm(forms.ModelForm):
    class Meta:
        model = TimeTableRow
        fields = ("start_at", "duration")
