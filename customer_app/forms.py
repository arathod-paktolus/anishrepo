from django import forms
from .models import Student
# from cryptography.fernet import Fernet




# def generate_key():
#     return Fernet.generate_key()
#
# key = generate_key()
#
# def encrypt_image_path(key, image_path):
#     cipher_suite = Fernet(key)
#     cipher_text = cipher_suite.encrypt(image_path.encode())
#     return cipher_text
#
# def decrypt_image_path(key, encrypted_image_path):
#     cipher_suite = Fernet(key)
#     plain_text = cipher_suite.decrypt(encrypted_image_path).decode()
#     return plain_text

# create a ModelForm
class StudentForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Student
        fields = "__all__"

    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     print('pan_card ==>', self.cleaned_data['pan_card'])
    #     encrypted_image_path = encrypt_image_path(key, self.cleaned_data['pan_card'])
    #     print('encrypted_image_path===>', encrypted_image_path)
    #     instance.pan_card = encrypted_image_path
    #
    #     if commit:
    #         instance.save()
    #     return instance

