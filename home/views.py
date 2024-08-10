from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home/home.html")

def about(request):
    return render(request, "about/about.html")

def services(request):
    return render(request, "services/services.html")

def contact(request):
    return render(request, "contact/contact.html")