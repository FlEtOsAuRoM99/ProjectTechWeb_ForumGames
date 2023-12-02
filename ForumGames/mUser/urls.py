
from django.urls import path, include, re_path
from . import views
from django.contrib.auth import views as auth_views

app_name="mUser"

urlpatterns = [
    path("account/login", auth_views.LoginView.as_view(template_name="html/account/login/Login.html"), name="Login"),
    path("account/logout", views.logout_req, name="Logout"),
    path("account/register", views.register_req, name="Register"),

]
