from django.urls import path
from . import views

# TEMPLATE URLS!

app_name = 'basic_app'

# URL PATTERNS!

urlpatterns = [
    path("register/", views.register, name="register"),
    path("user_login/", views.user_login, name="user_login"),
]