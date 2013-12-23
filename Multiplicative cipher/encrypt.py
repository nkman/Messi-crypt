import sys
alpha = 'ABCDEFGHIJKLMNNOPQRSTUVWXYZ'

def Ascii(key,a):
	return ((ord(a) - 65)*key % 26) + 65

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
	msg = msg.upper()
	key = raw_input('The key : ')
	key = int(key)
	sys.stdout.write(Encription(key,msg))

if __name__ == '__main__':
	main()

