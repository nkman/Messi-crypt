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

def Decryption(q,enr_txt):
	dec_txt = ''
	for m in enr_txt:
		if m in Alpha:
			num = ord(m) - q
			if m.isupper():
				if(num < 65):
					dec_txt = dec_txt + chr(num + 26)
				else:
					dec_txt = dec_txt + chr(num)
			else:
				if(num < 97):
					dec_txt = dec_txt + chr(num + 26)
				else:
					dec_txt = dec_txt + chr(num)
		else:
			dec_txt = dec_txt + m
	return dec_txt