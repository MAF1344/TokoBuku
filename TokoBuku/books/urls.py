from django.urls import path
from . import views

urlpatterns = [
    # authors url
    path("author/", views.author_list, name="author-list"),
    path("author/create/", views.author_create, name="author-create"),
    path("author/details/<int:id>/", views.author_details, name="author-details"),
    path("author/edit/<int:id>/", views.author_edit, name="author-edit"),
    path("author/delete/<int:id>/", views.author_delete, name="author-delete"),

    # categories url
    path("category/", views.category_list, name="category-list"),
    path("category/create/", views.category_create, name="category-create"),
    path("category/details/<int:id>/",
         views.category_details, name="category-details"),
    path("category/edit/<int:id>/", views.category_edit, name="category-edit"),
    path("category/delete/<int:id>/",
         views.category_delete, name="category-delete"),

    # books url
    path("", views.book_list, name="book-list"),
    path("create/", views.book_create, name="book-create"),
    path("details/<int:id>/", views.book_details, name="book-details"),
    path("edit/<int:id>/", views.book_edit, name="book-edit"),
    path("delete/<int:id>/", views.book_delete, name="book-delete"),
]
