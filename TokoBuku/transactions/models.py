# TokoBuku/transactions/models.py

from django.db import models
from TokoBuku.books.models import Book
from django.utils import timezone
# Impor settings untuk menggunakan AUTH_USER_MODEL
from django.conf import settings


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    book_name = models.CharField(max_length=200)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)  # Menambahkan default
    quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.book_name} - {self.quantity} pcs by {self.user.username} on {self.timestamp}"
