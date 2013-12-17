# ------ ----- ------- #
# Date - 16 Dec 2013
# Time - 9:55 PM
# Author - NKMAN
# It encrypts the text with 'CAESAR CIPHER' concept.
# ------ ----- ------- #

import sys
st = raw_input('Enter the string : ')
encrypted_text = ''
Alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
st = st.upper()
key = raw_input('Encryption Key ??')
key = int(key)
for m in st:
	if m in Alpha:
		num = ord(m) + key
		if(num > 90):
			encrypted_text = encrypted_text + chr(num - 26)
		else:
			encrypted_text = encrypted_text + chr(num)
	else:
		encrypted_text = encrypted_text + m

sys.stdout.write(encrypted_text.lower())