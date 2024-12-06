from django.urls import path
from . import views

urlpatterns = [
    path("", views.transaction_list, name="transaction-list"),
    path("create/<int:book_id>/", views.create_transaction,
         name="transaction-create"),  # Tambahkan ini
    path("details/<int:transaction_id>/",
         views.transaction_details, name="transaction-details"),
    path("delete/<int:transaction_id>/",
         views.transaction_delete, name="transaction-delete"),
]
