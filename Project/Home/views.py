from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"Home/index.html")

def contact(request):
    return render(request,"Home/index.html")

def products(request):
    return render(request,"Home/index.html")

def about(request):
    return render(request,"Home/_about.html")