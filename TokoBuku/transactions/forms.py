from django import forms
from .models import Transaction


class TransactionForm(forms.ModelForm):
    quantity = forms.IntegerField(label='Quantity', min_value=1)
    book_name = forms.CharField(
        label='Book Name', max_length=255, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    price = forms.CharField(label='Price', max_length=255,
                            widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Transaction
        fields = ['book_name', 'price', 'quantity']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        # Validasi untuk memastikan bahwa input adalah angka
        if not price.replace('.', '', 1).isdigit():
            raise forms.ValidationError("Price must be a valid number.")
        return price
