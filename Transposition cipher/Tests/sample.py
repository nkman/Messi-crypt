text = 'Forget the earth, Hez got the urge to pull his dick from the dirt and fuck the whole universe'
key = 8
import sys
for i in range(0,len(text)):
	sys.stdout.write(text[i] + ' ')
	i = i + 1
	if(i%key == 0):
		print ''