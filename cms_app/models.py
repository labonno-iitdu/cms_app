from django.db import models

class single_contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
