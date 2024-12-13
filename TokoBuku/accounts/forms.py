from django import forms
from .models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=False,
        help_text="Kosongkan jika tidak ingin mengubah password."
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_staff']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Masukkan username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Masukkan email'}),
        }
        help_texts = {
            'username': None,
            'email': None,
            'is_staff': "Centang jika pengguna adalah staff.",
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Ambil request jika ada
        super().__init__(*args, **kwargs)

        if not (self.request and self.request.user.is_superuser):
            self.fields.pop('is_staff')

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data.get("password"):
            user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    def clean_is_staff(self):
        is_staff = self.cleaned_data.get('is_staff', False)

        # Validasi hanya superuser yang dapat mengubah status staff
        if is_staff and not (self.request and self.request.user.is_superuser):
            raise forms.ValidationError(
                "Hanya superuser yang dapat mengatur status staff.")
        return is_staff
