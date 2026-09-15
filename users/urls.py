from django.urls import path
from .views import (
UserLoginView, 
UserLogoutView, 
SignupView, 
BecomeArtistView,
ProfileView,
MyPasswordResetCompleteView,
MyPasswordResetConfirmView,
MyPasswordResetDoneView,
MyPasswordResetView
)
urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("signup/",SignupView.as_view(),name="signup"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("become-artist/", BecomeArtistView.as_view(), name="become_artist"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("password-reset/",MyPasswordResetView.as_view(), name="password_reset"),
    path("password-reset-done/",MyPasswordResetDoneView.as_view(), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/",MyPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("password-reset-complete/",MyPasswordResetCompleteView.as_view(), name="password_reset_complete"),
]