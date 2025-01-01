from django.urls import path
from . import views

urlpatterns = [
    path("", views.first_website, name="index"),
    path("", views.prodoct_list, name='product_list'),
]

