from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("contact/",views.contact),
    path("products/",views.products),
    path("about/",views.about),
]