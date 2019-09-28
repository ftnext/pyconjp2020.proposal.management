from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_POST


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


def table_detail(request, pk):
    timetable = get_object_or_404(TimeTable, pk=pk)
    return render(
        request, "timetables/table_detail.html", {"timetable": timetable}
    )


@require_POST
def table_new(request):
    form = TimeTableForm(request.POST)
    if form.is_valid():
        timetable = form.save()
        return redirect("timetables:table_detail", pk=timetable.pk)
