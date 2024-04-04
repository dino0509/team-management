from django.urls import path

from . import views

app_name = "member_management"
urlpatterns = [
    path("", views.list, name="list"),
    path("add", views.add, name="add"),
    path("edit/<int:member_id>", views.edit, name="edit"),
    path("submit_edit/<int:member_id>", views.submit_edit, name="submit_edit"),
    path("submit_add", views.submit_add, name="submit_add"),
]
