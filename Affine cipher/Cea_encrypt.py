import sys
Alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Alpha = Alpha + Alpha.lower()

def Encryption(key,st):
	encrypted_text = ''
	for m in st:
		if m in Alpha:
			num = ord(m) + key
			if m.isupper():
				if(num > 90):
					encrypted_text = encrypted_text + chr(num - 26)
				else:
					encrypted_text = encrypted_text + chr(num)
			else:
				if(num > 122):
					encrypted_text = encrypted_text + chr(num - 26)
				else:
					encrypted_text = encrypted_text + chr(num)
		else:
			encrypted_text = encrypted_text + m
	return encrypted_text

def main():
	st = raw_input('Enter the string : ')
	key = raw_input('Encryption Key ?? : ')
	key = int(key)
	sys.stdout.write(Encryption(key,st))

if __name__ == "__main__":
	main()