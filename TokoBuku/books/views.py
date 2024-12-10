from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm


# Daftar buku
@login_required
def book_list(request):
    books = Book.objects.all()  # Mengambil semua buku dari database
    return render(request, "books/book-list.html", {'books': books})


def format_currency(value):
    return f"Rp. {value:,.0f}".replace(',', '.') + ',-'


# Detail buku
@login_required
def book_details(request, id):
    book = get_object_or_404(Book, id=id)
    formatted_price = format_currency(book.price)  # Format harga
    return render(request, 'books/book-details.html', {'book': book, 'formatted_price': formatted_price})


# Membuat buku baru
@login_required
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)  # Mengambil data dari form
        if form.is_valid():  # Memeriksa validitas data
            form.save()  # Menyimpan buku baru ke database
            # Redirect ke daftar buku setelah berhasil
            return redirect('book-list')
    else:
        form = BookForm()  # Membuat instance form kosong
    return render(request, "books/book-create.html", {'form': form})


# Edit buku
@login_required
def book_edit(request, id):
    book = get_object_or_404(Book, id=id)  # Mengambil buku berdasarkan ID
    if request.method == "POST":
        # Mengambil data dari form dan mengaitkan dengan buku yang ada
        form = BookForm(request.POST, instance=book)
        if form.is_valid():  # Memeriksa validitas data
            form.save()  # Memperbarui buku di database
            # Redirect ke detail buku setelah berhasil
            return redirect('book-details', id=book.id)
    else:
        # Membuat instance form dengan data buku yang ada
        form = BookForm(instance=book)
    return render(request, "books/book-edit.html", {'form': form})


# Hapus buku
@login_required
def book_delete(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        # Ambil nama buku dari form
        book_name_input = request.POST.get('title', '').strip()
        print(f"Input dari admin: '{book_name_input}'")  # Debugging
        print(f"Nama buku di database: '{book.title}'")  # Debugging

       # Periksa apakah nama buku yang dimasukkan sesuai
        if book_name_input == book.title:
            book.delete()  # Hapus buku jika nama sesuai
            # Redirect ke daftar buku setelah berhasil
            return redirect('book-list')
        else:
            error_message = "Nama buku salah. Silakan coba lagi."
            return render(request, "books/book-delete.html", {'book': book, 'error_message': error_message})

    return render(request, "books/book-delete.html", {'book': book})
