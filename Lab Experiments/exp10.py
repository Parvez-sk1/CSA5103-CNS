m = [
"MFHIK",
"UNOPQ",
"ZVWXY",
"ELARG",
"DSTBC"
]

text = "MUSTSEEYOUOVERCADOGANWESTCOMINGATONCE"
text = text.replace("J", "I")

def pos(c):
    for i in range(5):
        for j in range(5):
            if m[i][j] == c:
                return i, j

def enc(a, b):
    r1,c1 = pos(a)
    r2,c2 = pos(b)

    if r1 == r2:
        return m[r1][(c1+1)%5] + m[r2][(c2+1)%5]
    if c1 == c2:
        return m[(r1+1)%5][c1] + m[(r2+1)%5][c2]
    return m[r1][c2] + m[r2][c1]


p = []
i = 0
while i < len(text):
    a = text[i]
    b = text[i+1] if i+1 < len(text) else 'X'
    if a == b:
        b = 'X'
        i += 1
    else:
        i += 2
    p.append(a+b)

cipher = ''.join(enc(a,b) for a,b in p)

print("Pairs:", " ".join(p))
print("Cipher:", cipher)



'''
output: 
Pairs: MU ST SE EY OU OV ER CA DO GA NW ES TC OM IN GA TO NC EX
Cipher: KLHOQHTSCPLZQJYIQSABHAGQBNANQAK
'''
