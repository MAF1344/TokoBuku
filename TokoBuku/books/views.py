from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Author, Category
from .forms import BookForm, AuthorForm, CategoryForm
from .utils import admin_only


""" -------------- Views for books -------------- """


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


""" -------------- Views for authors -------------- """


# Daftar author
@login_required
@admin_only
def author_list(request):
    authors = Author.objects.all()  # Mengambil semua author dari database
    return render(request, "authors/author-list.html", {'authors': authors})


# Detail author
@login_required
@admin_only
def author_details(request, id):
    author = get_object_or_404(Author, id=id)
    return render(request, 'authors/author-details.html', {'author': author})


# Membuat author baru
@login_required
@admin_only
def author_create(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)  # Mengambil data dari form
        if form.is_valid():  # Memeriksa validitas data
            form.save()  # Menyimpan author baru ke database
            # Redirect ke daftar author setelah berhasil
            return redirect('author-list')
    else:
        form = AuthorForm()  # Membuat instance form kosong
    return render(request, "authors/author-create.html", {'form': form})


# Edit author
@login_required
@admin_only
def author_edit(request, id):
    # Mengambil author berdasarkan ID
    author = get_object_or_404(Author, id=id)
    if request.method == "POST":
        # Mengambil data dari form dan mengaitkan dengan author yang ada
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():  # Memeriksa validitas data
            form.save()  # Memperbarui author di database
            # Redirect ke detail author setelah berhasil
            return redirect('author-details', id=author.id)
    else:
        # Membuat instance form dengan data author yang ada
        form = AuthorForm(instance=author)
    return render(request, "authors/author-edit.html", {'form': form})


# Hapus author
@login_required
@admin_only
def author_delete(request, id):
    author = get_object_or_404(Author, id=id)

    if request.method == "POST":
        # Ambil nama author dari form
        author_name_input = request.POST.get('name', '').strip()
        print(f"Input dari admin: '{author_name_input}'")  # Debugging
        print(f"Nama author di database: '{author.name}'")  # Debugging

       # Periksa apakah nama author yang dimasukkan sesuai
        if author_name_input == author.name:
            author.delete()  # Hapus author jika nama sesuai
            # Redirect ke daftar author setelah berhasil
            return redirect('author-list')
        else:
            error_message = "Nama author salah. Silakan coba lagi."
            return render(request, "authors/author-delete.html", {'author': author, 'error_message': error_message})

    return render(request, "authors/author-delete.html", {'author': author})


""" -------------- Views for categories -------------- """


# Daftar kategori
@login_required
@admin_only
def category_list(request):
    categories = Category.objects.all()  # Mengambil semua kategori dari database
    return render(request, "categories/category-list.html", {'categories': categories})


# Detail kategori
@login_required
@admin_only
def category_details(request, id):
    # Mengambil kategori berdasarkan ID
    category = get_object_or_404(Category, id=id)
    return render(request, 'categories/category-details.html', {'category': category})


# Membuat kategori baru
@login_required
@admin_only
def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)  # Mengambil data dari form
        if form.is_valid():  # Memeriksa validitas data
            form.save()  # Menyimpan kategori baru ke database
            # Redirect ke daftar kategori setelah berhasil
            return redirect('category-list')
    else:
        form = CategoryForm()  # Membuat instance form kosong
    return render(request, "categories/category-create.html", {'form': form})


# Edit kategori
@login_required
@admin_only
def category_edit(request, id):
    # Mengambil kategori berdasarkan ID
    category = get_object_or_404(Category, id=id)
    if request.method == "POST":
        # Mengambil data dari form dan mengaitkan dengan kategori yang ada
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():  # Memeriksa validitas data
            form.save()  # Memperbarui kategori di database
            # Redirect ke detail kategori setelah berhasil
            return redirect('category-details', id=category.id)
    else:
        # Membuat instance form dengan data kategori yang ada
        form = CategoryForm(instance=category)
    return render(request, "categories/category-edit.html", {'form': form})


# Hapus kategori
@login_required
@admin_only
def category_delete(request, id):
    category = get_object_or_404(Category, id=id)

    if request.method == "POST":
        # Ambil nama kategori dari form
        category_name_input = request.POST.get('name', '').strip()
        print(f"Input dari admin: '{category_name_input}'")  # Debugging
        print(f"Nama kategori di database: '{category.name}'")  # Debugging

       # Periksa apakah nama kategori yang dimasukkan sesuai
        if category_name_input == category.name:
            category.delete()  # Hapus kategori jika nama sesuai
            # Redirect ke daftar kategori setelah berhasil
            return redirect('category-list')
        else:
            error_message = "Nama kategori salah. Silakan coba lagi."
            return render(request, "categories/category-delete.html", {'category': category, 'error_message': error_message})

    return render(request, "categories/category-delete.html", {'category': category})
