from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import About


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


def frontpage(request):
    return render(request, 'frontpage.html')


def contact_page(request):
    return render(request, 'contact.html')
