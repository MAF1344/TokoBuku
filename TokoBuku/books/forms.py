from django import forms
from .models import Book, Author, Category


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date', 'bio']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'published_year',
                  'author', 'synopsis', 'category']
