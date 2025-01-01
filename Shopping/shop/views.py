from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
# Create your views here.
def first_website(requests):
    return render(requests, 'rawr.html')

def search(request):
    query = request.GET.get('q', '')  # Get the search query from the URL
    results = []
    if query:
        results = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )  # Search in title or author
    return render(request, 'rawr.html', {'query': query, 'results': results})

def prodoct_list(requests):
    products = Product.objects.all()
    return render(requests, "rawr.html", {"Product" : products})