from django.shortcuts import render

# Create your views here.
def first_website(requests):
    return render(requests, 'rawr.html')

def search(requests):
    query = requests.GET.get("q")
    results = []
    pass