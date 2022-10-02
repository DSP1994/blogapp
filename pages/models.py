from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
