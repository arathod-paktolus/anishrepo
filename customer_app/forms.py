from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.exceptions import ValidationError as DjangoValidationError
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


    def clean_applicant_name(self):
        applicant_name = self.cleaned_data['applicant_name']
        if len(applicant_name) < 3:
            raise forms.ValidationError("applicant_name must be at least 3 characters long")
        return applicant_name
    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError('Must be at least 18 years old to register')
        return age

    def clean_contact_person_name(self):
        contact_person_name = self.cleaned_data.get('contact_person_name')

        # check if the contact_person_name contains only letters
        if not contact_person_name.isalpha():
            raise ValidationError('Contact person name should contain only letters')

        return contact_person_name

    def clean_email(self):
        valemail = self.cleaned_data['email']
        if len(valemail) < 10:
            raise forms.ValidationError('Enter more than or equal 4 char')
        return valemail

    def clean_mobile_number(self):
        mobile_number = str(self.cleaned_data.get('mobile_number'))

        if not mobile_number or len(mobile_number) != 10 or not mobile_number.isdigit():
            raise forms.ValidationError('Invalid mobile number. Please enter a 10-digit number.')

        return mobile_number
    def clean_zip_code(self):
        zip_code = self.cleaned_data.get('zip_code')

        if not isinstance(zip_code, int):
            raise forms.ValidationError('Zip code must be an integer.')

        return zip_code

