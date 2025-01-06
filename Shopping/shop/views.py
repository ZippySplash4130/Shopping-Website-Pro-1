from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
# Create your views here.
def first_website(requests):
    return render(requests, 'rawr.html')

def sign_up(requests):
    return render(requests, "signup.html")
