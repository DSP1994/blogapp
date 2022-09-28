from django.shortcuts import render


def frontpage(request):
    return render(request, 'frontpage.html')


def about_page(request):
    return render(request, 'about.html')


def contact_page(request):
    return render(request, 'contact.html')