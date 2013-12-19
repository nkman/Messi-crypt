import sys

def decrypt(key, message):
	size = len(message)
	code = ['']*size
	rows = size/key
	gap = size - rows*key
	k = 0
	for i in range(0,key/2-gap):
		for j in range(i,size):
			code[j] = message[k]
			k = k + 1
			j = j + 8

	for i in range(key/2-gap,key/2):
		

# code[0] = message[0], code[8] = message[1], code[16] = message[2], code[24] = message[3]
# 