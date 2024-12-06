from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TokoBuku.accounts.urls')),
    path("common/", include("TokoBuku.common.urls")),
    path("books/", include("TokoBuku.books.urls")),
    path("transactions/", include("TokoBuku.transactions.urls")),
]
