# # from cryptography.fernet import Fernet
# from cryptography.fernet import Fernet
#
# key = Fernet.generate_key()
# k = Fernet(key)
# # k.encrypt('test')
#
# token = k.encrypt('test')
# # Fernet.generate_key()

from cryptography.fernet import Fernet

# import base64
# Put this somewhere safe!
key = Fernet.generate_key()

f = Fernet(key)
token = f.encrypt(b"A really secret message. Not for prying eyes.")
print(f.decrypt(token))