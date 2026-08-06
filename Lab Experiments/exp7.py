
ciphertext = """53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83
(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8*
;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81
(‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;"""

mapping = {
    '5': 'a',
    '3': 'g',
    '‡': 'e',
    '†': 't',
    '8': 'h',
    ';': 'o'
}

plaintext = ""

for ch in ciphertext:
    if ch in mapping:
        plaintext += mapping[ch]
    else:
        plaintext += "_"

print("Ciphertext:\n")
print(ciphertext)

print("\n\nPartially Decrypted Text:\n")
print(plaintext)

'''
Ciphertext:

53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83
(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8*
;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81
(‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;


Partially Decrypted Text:

agettea__th_o___h_e__e_o_h__the____a__ahoo_h_oe_htg
_hh_ato_h___hh_____ho_te__ha_oato______e__h_____a_h
o_____ao__te_hee______h_a_h_the__e_ha_eat_ha_teah___
_te__ha_hh_ha___g_ha_e_oa_____hh_e__
'''