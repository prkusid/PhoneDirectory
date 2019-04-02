from django.db import models

# Create your models here.
class PhoneDirectory(models.Model):
    name = models.CharField(max_length = 255)
    phone_no = models.IntegerField()
