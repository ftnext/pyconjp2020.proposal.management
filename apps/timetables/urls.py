from django.urls import path

from . import views


app_name = "timetables"
urlpatterns = [
    path("", views.table_list, name="table_list"),
    path("<uuid:pk>/", views.table_detail, name="table_detail"),
]
