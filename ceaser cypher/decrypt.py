import sys

enr_txt = raw_input('Encrypted text : ')
q = raw_input('key was : ')
q = int(q)
dec_txt = ''

enr_txt = enr_txt.upper()
Alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for m in enr_txt:
	if m in Alpha:
		num = ord(m) - q
		if(num < 65):
			dec_txt = dec_txt + chr(num + 26)
		else:
			dec_txt = dec_txt + chr(num)

print dec_txt.lower()