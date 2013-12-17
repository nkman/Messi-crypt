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
	code = raw_input('Text to be enrcypted : ')
	key = raw_input('Encryption key : ')
	sys.stdout.write(enrcypt(int(key),code))

if __name__ == '__main__':
	main()