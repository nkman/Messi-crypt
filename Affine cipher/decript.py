import Ceaser
import Multiplicative

def Decryption(key,msg):
	txt = Ceaser.Decryption(key,msg)
	txt = Multiplicative.Decryption(key,txt)
	return txt

def main():
	txt = raw_input('Encrypted text : ')
	key = raw_input('Encryption key : ')
	print Decryption(int(key),txt)

if __name__ == '__main__':
	main()