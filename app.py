import os
from aes import encrypt_cbc, decrypt_cbc
from pbkdf2 import gerar_chave_pbkdf2

def main():
    print("teste")
    
    #mensagem qualquer, com tamanho "quebrado" (não é múltiplo de 16)
    mensagem = "Mine has been a life of much shame - Osamu Dazai!"
    senha_usuario = "12344"
    
    print(f"1. Mensagem: '{mensagem}'")
    print(f"2. Senha do usuário: '{senha_usuario}'\n")
    
    chave_mestra, salt_gerado = gerar_chave_pbkdf2(senha_usuario)
    #vetor inicial aleatorio precisa ter exatos 16 bytes. 
    #os.urandom(16) gera bytes aleatórios de forma segura :)
    iv = os.urandom(16)
    
    #passa tudo pelo CBC
    texto_cifrado = encrypt_cbc(mensagem.encode('utf-8'), chave_mestra, iv)
    
    print(f"SALT (Guardar com o arquivo): {salt_gerado.hex()}")
    print(f"IV   (Guardar com o arquivo): {iv.hex()}")
    print(f"Cifra final ({len(texto_cifrado)} bytes): {texto_cifrado.hex()}")

    #descriptografar
    mensagem_recuperada_bytes = decrypt_cbc(texto_cifrado, chave_mestra, iv)
    mensagem_recuperada_texto = mensagem_recuperada_bytes.decode('utf-8')

    print(f"\nMensagem decodificada: '{mensagem_recuperada_texto}'")

    print(f"Chave Mestra: {chave_mestra.hex()}")

if __name__ == "__main__":
    main()
