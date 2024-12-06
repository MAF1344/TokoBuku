from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import UserForm


def authenticate_with_email(email, password):
    User = get_user_model()
    try:
        user = User.objects.get(email=email)
        if user.check_password(password):
            return user
    except User.DoesNotExist:
        return None


def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate_with_email(
            email, password)  # Gunakan metode kustom
        if user is not None:
            login(request, user)
            return redirect('profile-details')
        else:
            return render(request, "accounts/login-page.html", {"error": "Email atau Password salah"})
    return render(request, "accounts/login-page.html")


def register_page(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  # Simpan pengguna baru
            # Redirect ke halaman login setelah berhasil
            return redirect('login-page')
    else:
        form = UserForm()
    return render(request, "accounts/register-page.html", {'form': form})


@login_required
def profile_details(request):
    user = get_object_or_404(User, username=request.user.username)
    return render(request, "accounts/profile-details.html", {'user': request.user})


@login_required
def profile_edit(request):
    user = request.user
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()  # Perbarui profil pengguna
            # Redirect ke halaman detail profil setelah berhasil
            return redirect('profile-details')
    else:
        form = UserForm(instance=user)
    return render(request, "accounts/profile-edit.html", {'form': form})


def profile_delete(request):
    user = request.user
    error_message = None

    if request.method == "POST":
        username = request.POST.get('username')
        if username == user.username:
            user.delete()
            return redirect('login-page')
        else:
            error_message = "Username salah. Silakan coba lagi."
    return render(request, "accounts/profile-delete.html", {'user': user, 'error_message': error_message})
