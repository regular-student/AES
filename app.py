# teste aes.py
from utils import sub_word, rot_word, rcon
from key_expansion import key_expansion


# Código

chave_teste = bytes([0x00]) * 32

w = key_expansion(chave_teste)

print(f"Total de palavras: {len(w)}")  # Deve ser 60
print(f"\nPrimeiras 8 palavras (chave original):")
for i in range(8):
    print(f"w[{i}] = {[hex(b) for b in w[i]]}")

print(f"\nPalavra 8 (primeira expandida):")
print(f"w[8] = {[hex(b) for b in w[8]]}")

# palavra = [0x00, 0x00, 0x00, 0x00]
# i = 8 
# 
# print(f"Original: {[hex(b) for b in palavra]}")
# 
# # Passo 1: rot_word
# temp = rot_word(palavra)
# print(f"Após RotWord: {[hex(b) for b in temp]}")
# 
# # Passo 2: sub_word
# temp = sub_word(temp)
# print(f"Após SubWord: {[hex(b) for b in temp]}")
# 
# # Passo 3: rcon
# rcon_valor = rcon[i // 8]
# temp[0] = temp[0] ^ rcon_valor
# print(f"Após Rcon ({hex(rcon_valor)}): {[hex(b) for b in temp]}")

print(f"\nPalavra 9 (segunda expandida):")
print(f"w[9] = {[hex(b) for b in w[9]]}")

print(f"\nPalavra 10 (terceira expandida):")
print(f"w[10] = {[hex(b) for b in w[10]]}")

# Chave com padrão simples
chave_teste = bytes([
    0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08,
    0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f, 0x10,
    0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18,
    0x19, 0x1a, 0x1b, 0x1c, 0x1d, 0x1e, 0x1f, 0x20
])

w = key_expansion(chave_teste)

print("w[8]  =", [hex(b) for b in w[8]])
print("w[9]  =", [hex(b) for b in w[9]])
print("w[10] =", [hex(b) for b in w[10]])
print("w[11] =", [hex(b) for b in w[11]])
