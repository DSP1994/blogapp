from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'body',  'created_on')
    search_fields = ('name', 'email', 'body')
