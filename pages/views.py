from django.shortcuts import render
# from django.views import generic, View
# from .models import FrontPage


# class FrontPage(View):
#     model = FrontPage
#     template_name = 'frontpage.html'

def frontpage(request):
    return render(request, 'frontpage.html')


def about_page(request):
    return render(request, 'about.html')


def contact_page(request):
    return render(request, 'contact.html')
