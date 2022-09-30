from . import views
from django.urls import path


urlpatterns = [
    path('frontpage/', views.frontpage, name='frontpage'),
    path('contact/', views.contact_page, name='contact_page'),
    path('about/', views.AboutSect.as_view(), name='about/html'),
]