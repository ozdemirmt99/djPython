from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"Home/index.html",context={"content":"Home/_products.html"})

def contact(request):
    return render(request,"Home/index.html",context={"content":"Home/_contact.html"})

def products(request):
    return render(request,"Home/index.html",context={"content":"Home/_products.html"})

def about(request):
    return render(request,"Home/index.html",context={"content":"Home/_about.html"})