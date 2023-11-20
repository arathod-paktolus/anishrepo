from django.shortcuts import render, redirect
from .forms import StudentForm
from django.http import HttpResponse
import base64

import os
# from cryptography.fernet import Fernet

# Create your views here

def index_view(request):

    return render(request, 'customer_app/student.html')

def home_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            print('form--->', form.cleaned_data['pan_card'])
            pan_card = str((form.cleaned_data['pan_card'])).encode('utf-8')
            aadhar_card = str((form.cleaned_data['aadhar_card'])).encode('utf-8')
            print('pan_card--->', pan_card)
            print('aadhar_card--->', aadhar_card)
            # data return in the form  of imagess
            form.save()
        else:
            print(form.errors)
            return index_view(request)
    return render(request, 'customer_app/student.html', {'form': form})


def encoding_docs(s):
    sample_string = s
    sample_string_bytes = sample_string.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string

#
def decoding_docs(d):
    base64_string = d
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    return sample_string
