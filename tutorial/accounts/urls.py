from django.urls import path, reverse_lazy
from .views import (
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

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', view_profile, name='view_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('change-password', change_password, name='change_password'),

    path('reset-password', PasswordResetView.as_view(
        template_name='accounts/reset_password.html', 
        email_template_name='accounts/reset_password_email.html',
        success_url = reverse_lazy('accounts:password_reset_done')
        ), name='reset_password'),

    path('reset-password/done', PasswordResetDoneView.as_view(template_name='accounts/reset_password_done.html'), name='password_reset_done'),

    path('reset-password/confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(
        template_name='accounts/reset_password_confirm.html',
        success_url = reverse_lazy('accounts:password_reset_complete')
    ), name='password_reset_confirm'),

    path('reset/done', PasswordResetCompleteView.as_view(template_name='accounts/reset_password_complete.html'), name='password_reset_complete'),

]
