LETTERS = 'ABCDEFGHIJKLMNOPQRSTVUWXYZ '
ciphertext = 'XLMWDMWDERDIRGUBTXIHDQIWWEKI'

def decrypt(text,key):
    text=text.upper()
    plaintxt=''
    for s in text:
        plaintxt+=str(LETTERS[(LETTERS.find(s)-key) % 27])
    return plaintxt

for l in LETTERS:
    freq = ciphertext.count(l) / float(len(ciphertext))
    if freq >= 0.1:
        #if a letter appears %10 or more that means it can be 'E' so we are trying to shift letters by 4
        #because value of 'E' is 4
        key = LETTERS.find(chr(ord(l)-4)) 
        print("Possible key: "+str(key))
        print(decrypt(ciphertext,key))
