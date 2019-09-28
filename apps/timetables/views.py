from django.shortcuts import render

from .forms import TimeTableForm
from .models import TimeTable


def table_list(request):
    timetables = TimeTable.objects.order_by("created_date")
    form = TimeTableForm()
    return render(
        request,
        "timetables/table_list.html",
        {"form": form, "timetables": timetables},
    )
