from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.views import generic, View
from .models import Contact
from .forms import ContactForm


class ContactPage(View):
    model = Contact
    template_name = 'contact.html'

    def contact_form(request):
        form = ContactForm(request.POST)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Redirect Succesful!")
                return HttpResponseRedirect('/')
    
        context = {
            'name': name,
            'email': email,
            'body': body,
        }

        return render(request, "contact.html", context)


def about(request):
    return render(request, 'about.html')


def frontpage(request):
    return render(request, 'frontpage.html')
