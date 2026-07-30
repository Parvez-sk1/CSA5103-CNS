plain_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher_alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM"

plaintext = input("Enter the plaintext: ")

ciphertext = ""

for ch in plaintext:
    if ch.isupper():
        index = plain_alphabet.index(ch)
        ciphertext += cipher_alphabet[index]
    elif ch.islower():
        index = plain_alphabet.index(ch.upper())
        ciphertext += cipher_alphabet[index].lower()
    else:
        ciphertext += ch

print("Ciphertext:", ciphertext)

# OUTPUT
# Enter the plaintext: hello
# Ciphertext: itssg
