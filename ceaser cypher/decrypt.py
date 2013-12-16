import sys

enr_txt = raw_input('Encrypted text : ')
size = len(enr_txt)
q = raw_input('key was : ')
q = int(q)
dec_txt = ''

for i in range(0,size):
	asc = ord(enr_txt[i]) - q
	if(asc<97):
		dec_txt = dec_txt + chr(asc + 26)
	else:
		dec_txt = dec_txt + chr(ord(enr_txt[i]) - q)
print dec_txt