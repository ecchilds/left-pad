from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b'# congrats! you found the flag!\n# token: a6DFg89r2Yh9Z\ndef insertminer(filename):\n\tf = open(filename,"r+")\n\tpos = f.tell()\n\tline = f.readline()\n\twhile line != "":\n\t\tpos = f.tell()\n\t\tline = f.readline()\n\tf.seek(pos)\n\tf.write("<script>/*cryptominer here*/</script>\\n")\n\tf.close()')

key_file = open("access_key.txt", 'wb')
token_file = open("datastore.py", 'wb')

key_file.write(key)
token_file.write(token)

key_file.close()
token_file.close()
