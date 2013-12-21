import sys

def decrypt(key, message):
	size = len(message)
	code = ['']*size
	rows = size/key
	if(size%key != 0):
		rows = rows + 1
	gap = rows*key - size
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
	text = raw_input('Encrypted Text : ')
	key = raw_input('Key used : ')
	sys.stdout.write(decrypt(int(key),text))

if __name__ == '__main__':
	main()