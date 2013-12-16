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

print encrypted_text.lower()