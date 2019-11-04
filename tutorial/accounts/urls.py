from django.urls import path
from .views import (
    home,
    register,
    # login,
)

from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', register, name='register'),
]
