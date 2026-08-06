
import string

keyword = "CIPHER"

cipher_alphabet = ""
for ch in keyword:
    if ch not in cipher_alphabet:
        cipher_alphabet += ch

for ch in string.ascii_uppercase:
    if ch not in cipher_alphabet:
        cipher_alphabet += ch

plain_alphabet = string.ascii_uppercase

print("Plain Alphabet : ", plain_alphabet)
print("Cipher Alphabet:", cipher_alphabet)

encrypt_map = {}
decrypt_map = {}

for p, c in zip(plain_alphabet, cipher_alphabet):
    encrypt_map[p] = c
    decrypt_map[c] = p

plaintext = input("\nEnter Plaintext: ").upper()

ciphertext = ""
for ch in plaintext:
    if ch in encrypt_map:
        ciphertext += encrypt_map[ch]
    else:
        ciphertext += ch

print("Encrypted Text :", ciphertext)

decrypted = ""
for ch in ciphertext:
    if ch in decrypt_map:
        decrypted += decrypt_map[ch]
    else:
        decrypted += ch

print("Decrypted Text :", decrypted)

'''
Plain Alphabet :  ABCDEFGHIJKLMNOPQRSTUVWXYZ
Cipher Alphabet: CIPHERABDFGJKLMNOQSTUVWXYZ

Enter Plaintext: hello world
Encrypted Text : BEJJM WMQJH
Decrypted Text : HELLO WORLD
'''