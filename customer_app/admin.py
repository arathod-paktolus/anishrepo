from django.contrib import admin
from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['applicant_name', 'age', 'contact_person_name', 'email', 'mobile_number', 'address', 'zip', \
                    'aadhar_card', 'pan_card']


admin.site.register(Student, StudentAdmin)