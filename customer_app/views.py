from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
from django.http import HttpResponse

# from cryptography.fernet import Fernet
from cryptography.fernet import Fernet

import os
import hashlib
from cryptography.fernet import Fernet
import base64

# Create your views here

def index_view(request):

    return render(request, 'customer_app/student.html')

def home_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()


            '''
            # applicant_name = form.cleaned_data['applicant_name']
            # age = form.cleaned_data['age']
            # contact_person_name = form.cleaned_data['contact_person_name']
            # email = form.cleaned_data['email']
            # mobile_number = form.cleaned_data['mobile_number']
            # address = form.cleaned_data['address']
            # zip = form.cleaned_data['zip']
            # pan_card = form.cleaned_data['pan_card']
            # aadhar_card = form.cleaned_data['aadhar_card']
            print('form--->', form.cleaned_data['pan_card'])
            pan_card = form.cleaned_data['pan_card']
            aadhar_card = form.cleaned_data['aadhar_card']
            print('pan_card--->', pan_card)
            print('aadhar_card--->', aadhar_card)
            # data return in the form  of images
            # st = Student(applicant_name=applicant_name, age=age, contact_person_name=contact_person_name,
            #              email=email, mobile_number=mobile_number, address=address, zip=zip,
            #              pan_card=pan_card, aadhar_card=aadhar_card)
            # st.save()

            # image_path = form.cleaned_data['pan_card']
            # encoded_image = image_path.encode('utf-8')
            # encoded_image = base64.b64encode(image_path)
            # # encoded_image = encode_image(image_path)
            # decoded_image = image_path.decode('utf-8')
            # decoded_image = base64.b64decode(image_path)
            # print('encoded_image------------>', encoded_image)
            # print('decoded_image------>', decoded_image)

            ##########################################

            # Generate a random salt for each user
            # salt = os.urandom(32)
            # 
            # # Generate a key based on the password and salt
            # key = hashlib.pbkdf2_hmac('sha256', str(pan_card).encode('utf-8'), salt, 100000, dklen=32)
            # 
            # # Initialize Fernet with the encoded key
            # fernet = Fernet(base64.urlsafe_b64encode(key))
            # document_path = pan_card
            # pan_card = document_path + ".enc"  # Store the encrypted path
            # with open(document_path, 'rb') as file:
            #     data = file.read()
            # encrypted_data = fernet.encrypt(data)
            # with open(pan_card, "wb") as encrypted_file:
            #     encrypted_file.write(encrypted_data)
            # 
            # ###############
            # form.save()
            '''
        else:
            print(form.errors)
            return index_view(request)
    return render(request, 'customer_app/student.html', {'form': form})







'''
# def encoding_docs(s):
#     sample_string = s
#     sample_string_bytes = sample_string.encode("ascii")
#     base64_bytes = base64.b64encode(sample_string_bytes)
#     base64_string = base64_bytes.decode("ascii")
#     return base64_string
#
# #
# def decoding_docs(d):
#     base64_string = d
#     base64_bytes = base64_string.encode("ascii")
#     sample_string_bytes = base64.b64decode(base64_bytes)
#     sample_string = sample_string_bytes.decode("ascii")
#     return sample_string


# import base64

#
# def encode_image(image_path):
#     with open(image_path, "rb") as image_file:
#         # Read the image file in binary mode
#
#     return encoded_image
#
#
# def decode_image(encoded_image, output_path):
#     # Decode the base64-encoded image
#     decoded_image = base64.b64decode(encoded_image)
#
#     # Write the decoded image data to a new file
#     with open(output_path, "wb") as output_file:
#         output_file.write(decoded_image)
#
#
# # Example usage
#
#
# # Save the encoded image to a text file
# # with open("encoded_image.txt", "wb") as text_file:
# #     text_file.write(encoded_image)
#
# # Decode the image from the text file
# # with open("encoded_image.txt", "rb") as text_file:
# #     encoded_image_from_file = text_file.read()
#
# # decode_image(encoded_image_from_file, "path/to/your/decoded_image.jpg")
'''