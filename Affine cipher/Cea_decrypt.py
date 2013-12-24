import sys
Alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Alpha = Alpha + Alpha.lower()

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

def main():
	enr_txt = raw_input('Encrypted text : ')
	q = raw_input('key was : ')
	q = int(q)
	sys.stdout.write(Decryption(q,enr_txt))

if __name__ == "__main__":
	main()