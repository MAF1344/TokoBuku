from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.login_page, name="login-page"),
    path("register/", views.register_page, name="register-page"),
    path("details/", views.profile_details, name="profile-details"),
    path("edit/", views.profile_edit, name="profile-edit"),
    path("delete/", views.profile_delete, name="profile-delete"),
    path('logout/', auth_views.LogoutView.as_view(next_page='home-page'), name='logout'),
]
