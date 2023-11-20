from django import forms
from .models import Student


# create a ModelForm
class StudentForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Student
        fields = "__all__"

