#Esse arquivo junta todas as operações 

from utils import bytes_to_states, state_to_bytes, add_round_key, sub_bytes, shift_rows, mix_columns
from key_expansion import key_expansion

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
