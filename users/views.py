
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views import View

from .models import User
from .form import SignupFrom
from playlist.models import Playlist

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

    def get(self, request, *args, **kwargs):
        print("========== CONFIRM VIEW RUNNING ==========")
        print("UID:", kwargs.get("uidb64"))
        print("TOKEN RECEIVED:", bool(kwargs.get("token")))

        response = super().get(request, *args, **kwargs)

        print("VALID LINK:", self.validlink)

        return response




class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = "users/password_reset_done.html"


class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "users/password_reset_complete.html"


class SignupView(CreateView):
    form_class = SignupFrom
    template_name = "users/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = "users/login.html"


class UserLogoutView(LogoutView):
    next_page = "/"


class BecomeArtistView(View):

    def post(self, request):
        request.user.role = "artist"
        request.user.save()

        return redirect("profile")


class ProfileView(View):

    def get(self, request):
        user = request.user

        playlists = Playlist.objects.filter(
            user=request.user
        )

        return render(
            request,
            "users/profile.html",
            {
                "profile": user,
                "playlists": playlists,
            }
        )

