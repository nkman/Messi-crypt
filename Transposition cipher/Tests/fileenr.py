import sys

def enrcypt(key, message):
	code = ''
	size = len(message)
	for i in range(0,key):
		j = i
		while(j < size):
			code = code + message[j]
			j = j + key
	return code

def main():
	code = open('sample.txt','r').read()
	key = 10
	f = open('encryptedSample.txt','w')
	f.write(enrcypt(int(key),code))
	sys.stdout.write(enrcypt(int(key),code))

if __name__ == '__main__':
	main()