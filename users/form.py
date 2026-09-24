from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignupFrom(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["first_name", "last_name", "bio", "username", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")

        return email