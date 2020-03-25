plain_text = 'this is an encrypted message'
LETTERS = ' ABCDEFGHIJKLMNOPQRSTVUWXYZ'

def encrypt(text,key):
    text=text.upper()
    cipher_text=''
    for s in text:
        cipher_text+=LETTERS[((LETTERS.find(s))+key) % 27]
    return cipher_text

def decrypt(text,key):
    text=text.upper()
    plaintxt=''
    for s in text:
        plaintxt+=LETTERS[((LETTERS.find(s))-key) % 27]
    return plaintxt

print(encrypt(plain_text,4))
print("")
for i in range(1,len(LETTERS)):
    print(decrypt(encrypt(plain_text,4),i))
