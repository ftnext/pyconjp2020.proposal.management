from django.shortcuts import render


def table_list(request):
    return render(request, "timetables/table_list.html", {})
