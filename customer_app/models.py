from django.db import models
from django.conf import settings

# Create your models here.
class Customer(models.Model):

    # ROLE_CHOICES = (
    #     ('User', 'User'),
    #     ('Admin', 'Admin'),
    # )

    objects = None
    applicant_name = models.CharField(max_length=70)
    age = models.IntegerField(blank=True,null=True)
    contact_person_name = models.CharField(max_length=70,)
    email = models.EmailField(max_length=70)
    mobile_number = models.IntegerField(null=True, blank=True, unique=True)
    address = models.TextField()
    zip_code = models.IntegerField()
    aadhar_card = models.FileField(upload_to='', blank=False)
    pan_card = models.FileField(upload_to='', blank=False)


