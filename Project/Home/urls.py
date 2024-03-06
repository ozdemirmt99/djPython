from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("contact/",views.contact,{"content":"contact.html"}),
    path("products/",views.products,{"content":"products.html"}),
    path("about/",views.about),
]