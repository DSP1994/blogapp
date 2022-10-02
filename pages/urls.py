from . import views
from django.urls import path


urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('contact/', views.contact, name='contact_page'),
    path('about/', views.about, name='about'),
]
