# TokoBuku/transactions/views.py

from TokoBuku.books.models import Book
from .models import Transaction
from django.shortcuts import render, get_object_or_404, redirect
from .forms import TransactionForm
# Impor decorator untuk login
from django.contrib.auth.decorators import login_required


def format_currency(value):
    return f"Rp. {value:,.0f}".replace(',', '.') + ',-'


@login_required
def create_transaction(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.book = book  # Menyimpan objek Book
            transaction.book_name = book.title
            transaction.price = book.price
            transaction.save()
            return redirect('transaction-list')
    else:
        form = TransactionForm({
            'book_name': book.title,
            'price': book.price,
        })

    formatted_price = format_currency(book.price)

    return render(request, 'transactions/transaction-create.html', {
        'form': form,
        'book': book,
        'formatted_price': formatted_price
    })


def transaction_list(request):
    transactions = Transaction.objects.select_related(
        'book').all()  # Mengambil transaksi dengan relasi book
    return render(request, "transactions/transaction-list.html", {'transactions': transactions})


def transaction_details(request, transaction_id):
    # Mengambil transaksi berdasarkan ID
    transaction = get_object_or_404(Transaction, id=transaction_id)

    # Hitung total harga
    total_price = transaction.price * transaction.quantity
    formatted_total_price = format_currency(total_price)

    return render(request, "transactions/transaction-details.html", {
        'transaction': transaction,
        'formatted_total_price': formatted_total_price
    })


def transaction_delete(request, transaction_id):
    # Mengambil transaksi berdasarkan ID
    transaction = get_object_or_404(Transaction, id=transaction_id)
    if request.method == "POST":
        transaction.delete()  # Menghapus transaksi
        # Redirect ke daftar transaksi setelah berhasil
        return redirect('transaction-list')
    return render(request, "transactions/transaction-delete.html", {'transaction': transaction})
