import math

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

cipher1 = ord('B') - ord('A')   
cipher2 = ord('U') - ord('A')   

mappings = [
    ('E', 'T'),
    ('T', 'E')
]

for p1_char, p2_char in mappings:
    p1 = ord(p1_char) - ord('A')
    p2 = ord(p2_char) - ord('A')

    diff_p = (p1 - p2) % 26
    diff_c = (cipher1 - cipher2) % 26

    inv = mod_inverse(diff_p, 26)

    if inv is None:
        print(f"Mapping {p1_char}, {p2_char}: No modular inverse.")
        continue

    a = (diff_c * inv) % 26

    if math.gcd(a, 26) != 1:
        print(f"Mapping {p1_char}, {p2_char}: Invalid value of a.")
        continue

    b = (cipher1 - a * p1) % 26

    print(f"\nMapping: B -> {p1_char}, U -> {p2_char}")
    print("Possible Key:")
    print("a =", a)
    print("b =", b)

    '''
    Mapping: B -> E, U -> T
Possible Key:
a = 3
b = 15

Mapping: B -> T, U -> E
Possible Key:
a = 23
b = 6
    
    '''
