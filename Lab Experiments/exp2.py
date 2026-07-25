# Caesar Cipher Encryption

plaintext = input("Enter the plaintext: ")
k = int(input("Enter the shift value (1-25): "))

ciphertext = ""

for ch in plaintext:
    if ch.isupper():
        ciphertext += chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
    elif ch.islower():
        ciphertext += chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
    else:
        ciphertext += ch  # Keep spaces and special characters unchanged

print("Ciphertext:", ciphertext)