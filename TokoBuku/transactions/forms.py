from django import forms
from .models import Transaction


class TransactionForm(forms.ModelForm):
    """Form for creating or updating a transaction."""
    quantity = forms.IntegerField(label='Quantity', min_value=1)
    book_name = forms.CharField(
        label='Book Name', max_length=255, widget=forms.HiddenInput())
    price = forms.CharField(label='Price', max_length=255,
                            widget=forms.HiddenInput())

    class Meta:
        model = Transaction
        fields = ['book_name', 'price', 'quantity']

    def clean_price(self):
        """Validate that the price is a valid number."""
        price = self.cleaned_data.get('price')
        if not price.replace('.', '', 1).isdigit():
            raise forms.ValidationError("Price must be a valid number.")
        return price
