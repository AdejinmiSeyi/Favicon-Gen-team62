from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="home_page"),
  path("about/", views.about, name="about_page"),
  path("login/", views.login_page, name="login_page"),
  path("signup/", views.signup_page, name="signup_page"),
  path("contact/", views.contact_page, name="contact_page"),
  path("error/", views.error_page, name="error_page"),
  path("generate/", views.generate_page, name="generate_page"),
  path("imageGen/", views.imageGen_page, name="imageGen_page"),
]