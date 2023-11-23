# # # from cryptography.fernet import Fernet
# # from cryptography.fernet import Fernet
# #
# # key = Fernet.generate_key()
# # k = Fernet(key)
# # # k.encrypt('test')
# #
# # token = k.encrypt('test')
# # # Fernet.generate_key()
#
# from cryptography.fernet import Fernet
#
# # import base64
# # Put this somewhere safe!
# key = Fernet.generate_key()
#
# f = Fernet(key)
# token = f.encrypt(b"A really secret message. Not for prying eyes.")
# print(f.decrypt(token))
#
# #

import cv2
import numpy as np
import pytesseract
from bs4 import BeautifulSoup
import re
from PIL import Image, ImageDraw
import sqlite3
import os
import hashlib
from cryptography.fernet import Fernet
import base64


# Function to register a new user
def register_user():
    email = input('Enter your email: ')
    password = input('Enter your password: ')

    # Generate a random salt for each user
    salt = os.urandom(32)

    # Generate a key based on the password and salt
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=32)

    # Initialize Fernet with the encoded key
    fernet = Fernet(base64.urlsafe_b64encode(key))

    # Allow the user to upload KYC documents (images)
    num_documents = 3  # int(input('How many KYC documents do you want to upload? '))
    encrypted_image_paths = []  # Define the list here
    for i in range(num_documents):
        document_path = input(f'Enter the path for KYC document {i + 1}: ')
        encrypted_document_path = document_path + ".enc"  # Store the encrypted path
        encrypted_image_paths.append(encrypted_document_path)  # Append to the list

        # Encrypt and store each KYC document
        with open(document_path, 'rb') as file:
            data = file.read()
        encrypted_data = fernet.encrypt(data)
        with open(encrypted_document_path, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)

    # Store email, salt, key, and encrypted KYC document paths in the SQLite database
    db_path = r'C:\sqlite\pyproject1.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the user_data table if it doesn't exist
    # Modify the CREATE TABLE statement to include the 'role' column
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_data (
            email TEXT,
            salt BLOB,
            key BLOB,
            image_paths TEXT,
            role TEXT DEFAULT 'user'  -- Add the 'role' column with a default value
        )
    ''')

    # Insert the user data into the table as before
    cursor.execute('INSERT INTO user_data (email, salt, key, image_paths, role) VALUES (?, ?, ?, ?, ?)',
                   (email, salt, key, ','.join(encrypted_image_paths), 'user'))

    # Commit changes and close the connection
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # Call the user registration function
    register_user()
