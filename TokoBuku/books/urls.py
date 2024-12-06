from django.urls import path
from . import views

urlpatterns = [
    path("", views.book_list, name="book-list"),
    path("create/", views.book_create, name="book-create"),
    path("details/<int:id>/", views.book_details, name="book-details"),
    path("edit/<int:id>/", views.book_edit, name="book-edit"),
    path("delete/<int:id>/", views.book_delete, name="book-delete"),
]
