from django.contrib import admin
from .models import Customer

# Register your models here.

class CustomerImageAdmin(admin.ModelAdmin):
    list_display = ['applicant_name', 'age', 'contact_person_name', 'email', 'mobile_number', 'address',
                    'zip_code','aadhar_card','pan_card']

admin.site.register(Customer, CustomerImageAdmin)

