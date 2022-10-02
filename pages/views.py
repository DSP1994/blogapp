from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.views import generic, View


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def frontpage(request):
    return render(request, 'frontpage.html')
