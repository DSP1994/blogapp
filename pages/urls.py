from django.urls import path
from . import views

urlpatterns = [
    path('frontpage/', views.frontpage, name='frontpage'),
    path('contact/', views.contact_page, name='contact_page'),
    path('about/', views.about_page, name='about_page'),
]