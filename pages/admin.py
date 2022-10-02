from django.contrib import admin
from .models import About, Contact



@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'body',  'created_on')
    search_fields = ('name', 'email', 'body')
