import sys

def decrypt(key, message):  #8,Cenoonommstmme oo snnio. s s c.
	size = len(message) #30
	code = ['']*size #['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
	rows = size/key #3
	if(size%key != 0):
		rows = rows + 1
	gap = rows*key - size
	k = 0
	print rows
	print gap
	for i in range(0,key-gap):
		for j in range(i,size):
			code[j] = message[k]
			k = k + 1
			j = j + key

	for i in range(key-gap, key):
		for j in range(i, size):
			code[j] = message[k]
			k = k + 1
			j = j + key - 1
	print code
	#for i in range(key/2-gap,key/2):
	#	for j in range(i,size):
	#		code[j] = message[k]

# code[0] = message[0], code[8] = message[1], code[16] = message[2], code[24] = message[3]
# 

decrypt(4,'nkman')