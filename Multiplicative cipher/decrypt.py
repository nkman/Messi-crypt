import sys
alpha = 'ABCDEFGHIJKLMNNOPQRSTUVWXYZ'

def Ascii(msg):
	return ord(msg) - 65

def Decrypter(key,message):
	ed = ''
	for m in message:
		if m in alpha:
			for i in range(0,26):
				if ((i*key % 26) == Ascii(m)):
					ed = ed + chr(i+65)
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
