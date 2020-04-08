ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ENGLISH_WORDS = []
def get_data():
	dictionary = open("english_words.txt","r")
	for word in dictionary.read().split('\n'):
		ENGLISH_WORDS.append(word)
	dictionary.close()
def count_words(text):
	text = text.upper()
	words = text.split(' ')
	matches = 0
	for word in words:
		if word in ENGLISH_WORDS:
			matches = matches + 1
	return matches
def is_text_english(text):
	matches = count_words(text)
	if (float(matches) / len(text.split('\n'))) * 100 >= 80:
		return True
	return False
def caesar_crack(cipher_text):
	for key in range(len(ALPHABET)):
		plain_text = ''
		for c in cipher_text:
			plain_text+=str(ALPHABET[((ALPHABET.find(c))-key) % len(ALPHABET)])
		if is_text_english(plain_text):
			print("We have managed to crack Caesar cipher, the key is: %s, the message is %s" % (key,plain_text))
get_data()
encrypted = 'VJKUBKUBCBOGUUCIG'
caesar_crack(encrypted)
