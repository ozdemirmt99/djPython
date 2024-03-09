from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request,"Home/index.html",context={"content":"Home/_indexContent.html"})

def products(request):
    items=[x for x in range(20)]
    return render(request,"Home/index.html",context={"content":"Home/_products.html", "items":items})

def about(request):
    return render(request,"Home/index.html",context={"content":"Home/_about.html"})