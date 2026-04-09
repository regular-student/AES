#Esse arquivo junta todas as operações 

from key_expansion import key_expansion
from utils import (
    bytes_to_states, state_to_bytes, 
    add_round_key, sub_bytes, shift_rows, mix_columns, 
    pad, xor_bytes
)

def encrypt_block(mensagem_16_bytes, chave_32_bytes):
    # 1-> expande a chave
    w = key_expansion(chave_32_bytes)

    # 2-> converte a mensagem para matriz do state
    state = bytes_to_states(mensagem_16_bytes)

    # fase 1 
    state = add_round_key(state, w, 0)

    # fase 2
    for round_num in range(1, 14):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, w, round_num)

    # fase 3
    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, w, 14)

    return state_to_bytes(state)

## CBC
# O CBC evita que plaintexts gerem sempre os mesmos ciphertexts
# Basicamente a ideia é criar um vetor de inicialização, um bloco de 16 bytes aleatórios 


def encrypt_cbc(mensagem_bytes, chave_32_bytes, iv_16_bytes): 
    if len(iv_16_bytes) != 16:
        raise ValueError("O IV deve ter 16 bytes")

    # arruma o tamanho da mensagem com padding
    mensagem_padded = pad(mensagem_bytes)

    texto_cifrado = b"" 
    bloco_anterior = iv_16_bytes

    #caminha de 16 em 16 bytes
    for i in range(0, len(mensagem_padded), 16):
        #pega a fatia da rodada atual
        bloco_atual = mensagem_padded[i:i+16]

        #cbc
        bloco_misturado = xor_bytes(bloco_atual, bloco_anterior) 

        #usa o encrypt block 
        bloco_cifrado = encrypt_block(bloco_misturado, chave_32_bytes)

        #salva o resultado
        texto_cifrado += bloco_cifrado
        bloco_anterior = bloco_cifrado

    return texto_cifrado
