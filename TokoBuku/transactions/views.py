from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from TokoBuku.books.models import Book
from .models import Transaction
from .forms import TransactionForm


def format_currency(value):
    """Format currency to Indonesian Rupiah."""
    return f"Rp. {value:,.0f}".replace(',', '.') + ',-'


@login_required
def create_transaction(request, book_id):
    """Create a new transaction for a specific book."""
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.book = book
            transaction.book_name = book.title
            transaction.price = book.price
            transaction.save()
            return redirect('transaction-list')
    else:
        form = TransactionForm(initial={
            'book_name': book.title,
            'price': format_currency(book.price),  # Format price for display
        })

    return render(request, 'transactions/transaction-create.html', {
        'form': form,
        'book': book,
    })


def transaction_list(request):
    """List all transactions."""
    transactions = Transaction.objects.select_related('book').all()
    return render(request, "transactions/transaction-list.html", {'transactions': transactions})


def transaction_details(request, transaction_id):
    """Display details of a specific transaction."""
    transaction = get_object_or_404(Transaction, id=transaction_id)
    total_price = transaction.price * transaction.quantity
    formatted_total_price = format_currency(total_price)

    return render(request, "transactions/transaction-details.html", {
        'transaction': transaction,
        'formatted_total_price': formatted_total_price
    })


def transaction_delete(request, transaction_id):
    """Delete a specific transaction."""
    transaction = get_object_or_404(Transaction, id=transaction_id)
    if request.method == "POST":
        transaction.delete()
        return redirect('transaction-list')
    return render(request, "transactions/transaction-delete.html", {'transaction': transaction})
