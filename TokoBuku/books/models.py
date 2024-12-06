from django.db import models

# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)  # ID otomatis
    title = models.CharField(max_length=200)  # Nama buku
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Harga buku
    published_year = models.PositiveIntegerField()  # Tahun terbit
    author = models.CharField(max_length=100)  # Nama penulis
    synopsis = models.TextField()  # Sinopsis singkat

    def __str__(self):
        return self.title  # Mengembalikan nama buku saat objek dicetak
