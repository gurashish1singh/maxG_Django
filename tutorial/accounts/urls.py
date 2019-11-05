from django.urls import path
from .views import (
    home,
    register,
    view_profile,
    edit_profile,
    change_password,
)

from django.contrib.auth.views import (
    LoginView, 
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
7

urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', view_profile, name='view_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('change-password', change_password, name='change_password'),
    path('reset-password', PasswordResetView.as_view(), name='reset_password'),
    path('reset-password/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
