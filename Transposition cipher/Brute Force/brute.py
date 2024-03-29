# ------ ----- ------- #
# Date - 23 Dec 2013
# Time - 1:50 PM
# Author - NKMAN
# It decrypts the text with 'Transposition CIPHER' concept with brute-force.
# ------ ----- ------- #

q = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ \t\n'
from decrypt import decrypt
import sys
#q = q + q.lower()
def remove(message):
	f = ''
	message = message.upper()
	for t in message:
		if t in q:
			f = f + t
	return f.split()

def DictionaryLoader():
	f = open('../dictionary.txt','r')
	words = []
	for t in f.read().split('\n'):
		words.append(t)
	f.close()
	return words

def main():
	msg = raw_input('Encrypted Text : ')
	for i in range(0,len(msg)):
		print 'Trying with key #%s' % i
		word = decrypt(i,msg)
		if(CountWords(word) > 0.2): #Assuming 20 percenteg of words
			print word
			sys.exit()
	print 'Sorry Could not find the type of encryption'
	sys.exit()

def CountWords(message):
	wordList = remove(message)
	if wordList == []:
		return 0
	count = 0
	for t in wordList:
		if t in DictionaryLoader():
			count += 1
	return float(count)/len(wordList)

if __name__ == '__main__':
	main()