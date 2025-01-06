from django.urls import path
from . import views

urlpatterns = [
    path("shop", views.first_website, name="index"),
    path("", views.sign_up, name="signup")
]

