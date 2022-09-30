from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import About


class AboutSect(generic.View):
    model = About
    queryset = About.objects.filter(status=1)
    template_name = about.html

# class FrontPage(View):
#     model = FrontPage
#     template_name = 'frontpage.html'

def frontpage(request):
    return render(request, 'frontpage.html')


def about_page(request):
    return render(request, 'about.html')


def contact_page(request):
    return render(request, 'contact.html')
