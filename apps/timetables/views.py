from django.shortcuts import render

from .forms import TimeTableForm


def table_list(request):
    form = TimeTableForm()
    return render(request, "timetables/table_list.html", {"form": form})
