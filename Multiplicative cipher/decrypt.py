# ------ ----- ------- #
# Date - 23 Dec 2013
# Time - 7:28 PM
# Author - NKMAN
# It decripts the text with 'Multiplicative CIPHER' concept.
# ------ ----- ------- #

import sys
alpha = 'ABCDEFGHIJKLMNNOPQRSTUVWXYZ'
alpha = alpha + alpha.lower()

def Ascii(msg):
	if msg.isupper():
		return ord(msg) - 65
	else:
		return ord(msg) - 97

def Decrypter(key,message):
	ed = ''
	for m in message:
		if m in alpha:
			for i in range(0,26):
				if ((i*key % 26) == Ascii(m)):
					if m.isupper():
						ed = ed + chr(i+65)
					else:
						ed = ed + chr(i+97)
					break
		else:
			ed = ed + m
	return ed

def main():
	msg = raw_input('Encrypted Text : ')
	key = raw_input('Encription key : ')
	key = int(key)
	sys.stdout.write(Decrypter(key,msg))

if __name__ == '__main__':
	main()