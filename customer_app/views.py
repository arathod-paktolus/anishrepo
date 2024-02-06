from django.shortcuts import render
from .forms import CustomerForm
from Crypto.Cipher import AES
from PIL import Image
from .models import Customer
import os
from django.http import HttpResponse
from django.contrib import messages


def home_view(request):
    context = {}

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)

        if form.is_valid():
            applicant_name = form.cleaned_data.get('applicant_name')
            age = form.cleaned_data.get('age')
            contact_person_name = form.cleaned_data.get('contact_person_name')
            email = form.cleaned_data.get('email')
            mobile_number = form.cleaned_data.get('mobile_number')
            address = form.cleaned_data.get('address')
            zip_code = form.cleaned_data.get('zip_code')
            aadhar_card = form.cleaned_data['aadhar_card']
            pan_card = form.cleaned_data['pan_card']

            # Perform encryption logic
            key = b'abcdefghijklmnop'
            cipher = AES.new(key, AES.MODE_EAX)
            try:
                # Process Aadhar Card image
                aadhar_card_image = Image.open(aadhar_card)
                cipher_aadhar = AES.new(key, AES.MODE_EAX)     # New cipher instance for Aadhar card
                # Use 'decrypted_pan_image' as needed (e.g., save to a file or display)
                encrypted_image, MAC_val = cipher_aadhar.encrypt_and_digest(aadhar_card_image.tobytes())

                # Save encrypted data to .txt file and update the form field
                aadhar_card_txt_path = save_encrypted_data_to_file(aadhar_card, encrypted_image, MAC_val)
                form.cleaned_data['aadhar_card'] = aadhar_card_txt_path

                # Perform decryption logic for Aadhar Card
                decrypted_aadhar_image = decrypt_image(aadhar_card_txt_path, key)
                # Use 'decrypted_aadhar_image' as needed (e.g., save to a file or display)

                # Process Pan Card image
                pan_card_image = Image.open(pan_card)
                cipher_pan = AES.new(key, AES.MODE_EAX)  # New cipher instance for PAN card
                encrypted_image, MAC_val = cipher_pan.encrypt_and_digest(pan_card_image.tobytes())

                # Save encrypted data to .txt file and update the form field
                pan_card_txt_path = save_encrypted_data_to_file(pan_card, encrypted_image, MAC_val)
                form.cleaned_data['pan_card'] = pan_card_txt_path

                # Perform decryption logic for Pan Card
                decrypted_pan_image = decrypt_image(pan_card_txt_path, key)

                # Save form data and file paths into the database
                form.save()

            except Exception as e:
                # Handle any potential exceptions during encryption or decryption
                error_message = f"An error occurred: {e}"
                return HttpResponse(error_message)

            messages.add_message(request,messages.SUCCESS,"Your Data has been submitted !!!")
    else:
        form = CustomerForm()

    context['form'] = form
    return render(request, 'customer_app/customer.html', context)


def save_encrypted_data_to_file(original_file, encrypted_data, mac_value):
    # Create a .txt file path based on the original file's name
    txt_file_path = os.path.join(f"{os.path.splitext(original_file.name)[0]}.txt")

    # Save encrypted data to the .txt file
    with open(txt_file_path, 'wb') as f:
        f.write(encrypted_data)
        f.write(mac_value)

    return txt_file_path


def decrypt_image(encrypted_txt_path, key):
    # Read encrypted data from the .txt file
    with open(encrypted_txt_path, 'rb') as f:
        encrypted_data = f.read()

    # Separate the encrypted data and MAC value
    encrypted_data, mac_value = encrypted_data[:-16], encrypted_data[-16:]

    # Initialize the decryptor
    cipher = AES.new(key, AES.MODE_EAX)

    # Decrypt the data
    decrypted_data = cipher.decrypt(encrypted_data)

    # Create a PIL Image from the decrypted data
    # Assuming the image mode is 'RGB' and size is (width, height)
    mode = 'RGB'
    size = (100, 100)  # Replace with the actual size of your images
    decrypted_image = Image.frombytes(mode, size, decrypted_data)

    return decrypted_image
# =======
# from django.shortcuts import render, redirect
# from .forms import StudentForm
# from .models import Student
# from django.http import HttpResponse
#
# # from cryptography.fernet import Fernet
# from cryptography.fernet import Fernet
#
# import os
# import hashlib
# from cryptography.fernet import Fernet
# import base64
#
# # Create your views here
#
# def index_view(request):
#
#     return render(request, 'customer_app/student.html')
#
# def home_view(request):
#     form = StudentForm()
#     if request.method == 'POST':
#         form = StudentForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             form.save()
#
#
#             '''
#             # applicant_name = form.cleaned_data['applicant_name']
#             # age = form.cleaned_data['age']
#             # contact_person_name = form.cleaned_data['contact_person_name']
#             # email = form.cleaned_data['email']
#             # mobile_number = form.cleaned_data['mobile_number']
#             # address = form.cleaned_data['address']
#             # zip = form.cleaned_data['zip']
#             # pan_card = form.cleaned_data['pan_card']
#             # aadhar_card = form.cleaned_data['aadhar_card']
#             print('form--->', form.cleaned_data['pan_card'])
#             pan_card = form.cleaned_data['pan_card']
#             aadhar_card = form.cleaned_data['aadhar_card']
#             print('pan_card--->', pan_card)
#             print('aadhar_card--->', aadhar_card)
#             # data return in the form  of images
#             # st = Student(applicant_name=applicant_name, age=age, contact_person_name=contact_person_name,
#             #              email=email, mobile_number=mobile_number, address=address, zip=zip,
#             #              pan_card=pan_card, aadhar_card=aadhar_card)
#             # st.save()
#
#             # image_path = form.cleaned_data['pan_card']
#             # encoded_image = image_path.encode('utf-8')
#             # encoded_image = base64.b64encode(image_path)
#             # # encoded_image = encode_image(image_path)
#             # decoded_image = image_path.decode('utf-8')
#             # decoded_image = base64.b64decode(image_path)
#             # print('encoded_image------------>', encoded_image)
#             # print('decoded_image------>', decoded_image)
#
#             ##########################################
#
#             # Generate a random salt for each user
#             # salt = os.urandom(32)
#             #
#             # # Generate a key based on the password and salt
#             # key = hashlib.pbkdf2_hmac('sha256', str(pan_card).encode('utf-8'), salt, 100000, dklen=32)
#             #
#             # # Initialize Fernet with the encoded key
#             # fernet = Fernet(base64.urlsafe_b64encode(key))
#             # document_path = pan_card
#             # pan_card = document_path + ".enc"  # Store the encrypted path
#             # with open(document_path, 'rb') as file:
#             #     data = file.read()
#             # encrypted_data = fernet.encrypt(data)
#             # with open(pan_card, "wb") as encrypted_file:
#             #     encrypted_file.write(encrypted_data)
#             #
#             # ###############
#             # form.save()
#             '''
#         else:
#             print(form.errors)
#             return index_view(request)
#     return render(request, 'customer_app/student.html', {'form': form})


