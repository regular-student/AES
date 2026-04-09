import os
from aes import encrypt_cbc

def testar_cbc():
    print("teste")
    
    #mensagem qualquer, com tamanho "quebrado" (não é múltiplo de 16)
    mensagem_texto = "Mine has been a life of much shame - Osamu Dazai!"
    mensagem_bytes = mensagem_texto.encode('utf-8')
    
    print(f"Tamanho original da mensagem: {len(mensagem_bytes)} bytes")
    
    #chave fixa de 32 bytes para o teste
    chave = bytes([0x42] * 32) 
    
    #vetor inicial aleatorio precisa ter exatos 16 bytes. 
    #os.urandom(16) gera bytes aleatórios de forma segura :)
    iv = os.urandom(16)
    
    #passa tudo pelo CBC
    texto_cifrado = encrypt_cbc(mensagem_bytes, chave, iv)
    
    print(f"Tamanho do texto cifrado: {len(texto_cifrado)} bytes")
    print("\nTexto Cifrado (Hexadecimal):")
    print(texto_cifrado.hex())

if __name__ == "__main__":
    testar_cbc()
