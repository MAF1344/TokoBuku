from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import UserForm
from .utils import admin_only


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
        user = authenticate_with_email(email, password)
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
            form.save()
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
            form.save()
            return redirect('profile-details')
    else:
        form = UserForm(instance=user)
    return render(request, "accounts/profile-edit.html", {'form': form})


@login_required
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


""" ------------------- Admin Only ------------------- """


@admin_only
def profile_list(request):
    users = User.objects.all()
    return render(request, "accounts/profile-list.html", {'users': users})


@admin_only
def profile_details_admin(request, id):
    # Detail pengguna yang dilihat
    user_detail = get_object_or_404(User, id=id)

    # Tentukan role berdasarkan is_staff dan is_superuser
    if user_detail.is_staff and user_detail.is_superuser:
        role = "SuperUser"
    elif user_detail.is_staff:
        role = "Staff"
    else:
        role = "User"

    return render(request, 'accounts/profile-details-admin.html', {
        'user_detail': user_detail,  # Pengguna yang sedang dilihat
        'role': role,               # Role yang sudah dihitung
        'user': request.user,       # Pengguna yang sedang login
    })


@admin_only
def profile_edit_admin(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user, request=request)
        if form.is_valid():
            form.save()
            return redirect('profile-details-admin', id=id)
    else:
        form = UserForm(instance=user, request=request)
    return render(request, "accounts/profile-edit-admin.html", {'form': form})


@admin_only
def profile_delete_admin(request, id):
    user = get_object_or_404(User, id=id)
    error_message = None
    if request.method == "POST":
        username = request.POST.get('username')
        if username == user.username:
            user.delete()
            return redirect('profile-list')
        else:
            error_message = "Username salah. Silakan coba lagi."
    return render(request, "accounts/profile-delete-admin.html", {'user': user, 'error_message': error_message})
