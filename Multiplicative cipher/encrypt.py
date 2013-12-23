# ------ ----- ------- #
# Date - 23 Dec 2013
# Time - 7:21 PM
# Author - NKMAN
# It encripts the text with 'Multiplicative CIPHER' concept.
# ------ ----- ------- #

import sys
alpha = 'ABCDEFGHIJKLMNNOPQRSTUVWXYZ'
alpha = alpha + alpha.lower()

def Ascii(key,a):
	if a.isupper():
		return ((ord(a) - 65)*key % 26) + 65
	else:
		return ((ord(a) - 97)*key % 26) + 97

def Encription(key,message):
	ed = ''
	for t in message:
		if t in alpha:
			ed = ed + chr(Ascii(key,t))
		else:
			ed = ed + t
	return ed

def main():
	msg = raw_input('The text to be encrypted : ')
	#msg = msg.upper()
	key = raw_input('The key : ')
	key = int(key)
	sys.stdout.write(Encription(key,msg))

if __name__ == '__main__':
	main()