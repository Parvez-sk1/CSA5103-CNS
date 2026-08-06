import math

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def encrypt(text, a, b):
    if math.gcd(a, 26) != 1:
        print("Invalid value of 'a'. It must be coprime with 26.")
        return ""

    result = ""

    for ch in text.upper():
        if ch.isalpha():
            p = ord(ch) - ord('A')
            c = (a * p + b) % 26
            result += chr(c + ord('A'))
        else:
            result += ch

    return result

def decrypt(cipher, a, b):
    if math.gcd(a, 26) != 1:
        print("Invalid value of 'a'.")
        return ""

    a_inv = mod_inverse(a, 26)
    result = ""

    for ch in cipher.upper():
        if ch.isalpha():
            c = ord(ch) - ord('A')
            p = (a_inv * (c - b)) % 26
            result += chr(p + ord('A'))
        else:
            result += ch

    return result

text = input("Enter Plaintext: ")
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

cipher = encrypt(text, a, b)

if cipher:
    print("Encrypted Text :", cipher)
    print("Decrypted Text :", decrypt(cipher, a, b))