from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import User
from playlist.models import Playlist
from django.shortcuts import redirect, render
from django.views import View
from .form import SignupFrom
from django.contrib.auth.views import (
    PasswordResetView,
    LoginView, 
    LogoutView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)


class MyPasswordResetView(PasswordResetView):
    template_name = "users/password_reset.html"
    email_template_name = "users/password_reset_email.html"
    subject_template_name = "users/password_reset_subject.txt"
    success_url = reverse_lazy("password_reset_done")

    def form_valid(self, form):
        print("========== FORM VALID ==========")
        print("EMAIL:", form.cleaned_data["email"])

        response = super().form_valid(form)

        print("========== EMAIL SENT ==========")

        return response

    def form_invalid(self, form):
        print("========== FORM INVALID ==========")
        print("ERRORS:", form.errors)

        return super().form_invalid(form)




class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "users/password_reset_confirm.html"

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = "users/password_reset_done.html"

class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "users/password_reset_complete.html"

class SignupView(CreateView):
    form_class = SignupFrom
    template_name = "users/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        User.objects.create(
            user=self.object
        )

        return response


class UserLoginView(LoginView):
    template_name = "users/login.html"


class UserLogoutView(LogoutView):
    next_page = "/"

class BecomeArtistView(View):

    def post(self, request):
        profile = request.user.profile

        profile.role = "artist"
        profile.save()

        User.objects.get_or_create(
            user=request.user,
            defaults={
                "name": request.user.username,
                "bio": ""
            }
        )

        return redirect("profile")

class ProfileView(View):

    def get(self, request):
        profile = request.user.profile
        playlists = Playlist.objects.filter(
            user=request.user
        )

        return render(
            request,
            "users/profile.html",
            {
                "profile": profile,
                "playlists": playlists,  

            }
        )      