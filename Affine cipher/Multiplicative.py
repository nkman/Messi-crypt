import sys
alpha = 'ABCDEFGHIJKLMNNOPQRSTUVWXYZ'
alpha = alpha + alpha.lower()

def AsciiD(msg):
	if msg.isupper():
		return ord(msg) - 65
	else:
		return ord(msg) - 97

def Decryption(key,message):
	ed = ''
	for m in message:
		if m in alpha:
			for i in range(0,26):
				if ((i*key % 26) == AsciiD(m)):
					if m.isupper():
						ed = ed + chr(i+65)
					else:
						ed = ed + chr(i+97)
					break
		else:
			ed = ed + m
	return ed

def Ascii(key,a):
	if a.isupper():
		return ((ord(a) - 65)*key % 26) + 65
	else:
		return ((ord(a) - 97)*key % 26) + 97

def Encryption(key,message):
	ed = ''
	for t in message:
		if t in alpha:
			ed = ed + chr(Ascii(key,t))
		else:
			ed = ed + t
	return ed