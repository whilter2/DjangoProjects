from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    return render(request, "home.html",{})

def photos(request):
    response = requests.get("https://jsonplaceholder.typicode.com/photos")
    data = response.json()
    context = {
        'photos': data
    }
    return render(request, "photos/index.html",context)