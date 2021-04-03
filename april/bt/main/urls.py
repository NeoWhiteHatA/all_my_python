from os import name
from re import template
from django.urls import path
from django.views.generic import TemplateView
from main import views

urlpatterns = [
    path(
        'contact_us/',
        views.ContactUsView.as_view(),
        name='contact_us',
    ),
    path(
        'about_us/',
        TemplateView.as_view(template_name='about_us.html'), 
        name = 'about_us',
        ),
    path('', TemplateView.as_view(template_name='home.html'),
         name = 'home',
         ),
    path("products/", TemplateView.as_view(template_name = 'product_list.html'), name="products")
]
