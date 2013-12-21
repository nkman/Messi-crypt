import sys

def decrypt(key, message):
	size = len(message)
	code = ['']*size
	k = 0
	for i in range(0,key):
		j = i
		while(j < size):
			code[j] = message[k]
			k = k + 1
			j = j + key
		i = i + 1
	return ''.join(code)

def main():
	text = open('encryptedSample.txt','r').read()
	key = 8
	sys.stdout.write(decrypt(int(key),text))

if __name__ == '__main__':
	main()