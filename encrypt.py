import sys
import time
st = raw_input('Enter the string : ')
encrypted_text = ''
string_size = len(st)
q = raw_input('Enter the key (0-25) : ')
q = int(q)
if(q>25 or q<0):
	sys.stdout.write("Enter within limits\nExiting...\n")
	time.sleep(1)
	exit()
i = 0
for i in range(0,string_size):
	encrypted_text = encrypted_text + chr(ord(st[i])+q)
	i = i + 1
print encrypted_text