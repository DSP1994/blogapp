from django.contrib import admin
from .models import About
from django_summernote import SummernoteModelAdmin

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    
# Register your models here.
