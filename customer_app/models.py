from django.db import models
from django.conf import settings

# Create your models here.


class Student(models.Model):
    # ROLE_CHOICES = (
    #     ('User', 'User'),
    #     ('Admin', 'Admin'),
    # )
    applicant_name = models.CharField(max_length=70)
    age = models.IntegerField(blank=True,null=True)
    contact_person_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    mobile_number = models.IntegerField(null=True, blank=True, unique=True)
    address = models.TextField()
    zip = models.IntegerField(max_length=10)
    aadhar_card = models.ImageField(upload_to='stud/images',  blank=True, null=True)
    print(aadhar_card.name)
    pan_card = models.ImageField(upload_to='stud/images',  blank=True, null=True)
    # role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.applicant_name

