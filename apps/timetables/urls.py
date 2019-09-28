from django.urls import path

from . import views


app_name = "timetables"
urlpatterns = [
    path("", views.table_list, name="table_list"),
    path("<uuid:pk>/", views.table_detail, name="table_detail"),
    path("new/", views.table_new, name="table_new"),
    path("<uuid:table_pk>/column_new/", views.column_new, name="column_new"),
    path("<uuid:table_pk>/row_new/", views.row_new, name="row_new"),
]
