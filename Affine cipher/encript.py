import Ceaser
import Multiplicative

def Encryption(key,msg):
	text = Multiplicative.Encryption(key,msg)
	text = Ceaser.Encryption(key,text)
	return text

def main():
	text = raw_input('Text to be Encrypted : ')
	key = raw_input('The key of Encryption (should be odd) : ')
	print Encryption(int(key),text)

if __name__ == '__main__':
	main()