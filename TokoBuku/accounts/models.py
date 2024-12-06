from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Menambahkan field email
    email = models.EmailField(max_length=254, unique=True)

    # Atribut yang diperlukan
    USERNAME_FIELD = 'username'  # Field yang digunakan untuk login
    # Field lain yang diperlukan saat membuat pengguna melalui createsuperuser
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
