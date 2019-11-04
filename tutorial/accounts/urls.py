from django.urls import path
from .views import (
    home,
    # login,
)

from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),

]
