from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.views import generic, View
from .models import About
from .forms import ContactForm


class AboutSect(generic.ListView):
    model = About
    queryset = About.objects.filter(status=1)
    template_name = 'about.html'


class AboutDetail(View):
   
    def get(self, request, slug, *args, **kwargs):
        queryset = Blog.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        
        return render(
            request,
            'about.html', {
                'post': post,
            },
        )


def contact_form(request):
    form = ContactForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Redirect Succesful!")
            return HttpResponseRedirect('/')
    
    context = {
        "form": form
    }

    return render(request, "contact.html", context)


def frontpage(request):
    return render(request, 'frontpage.html')


def contact_page(request):
    return render(request, 'contact.html')
