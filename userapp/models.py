from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    aadhar_number = models.CharField(max_length=8)
    unique_id = models.CharField(max_length=10)