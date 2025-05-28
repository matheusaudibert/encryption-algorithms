def decifra_de_vigenere(texto_cifrado, chave):
    resultado = ""
    chave = chave.lower()
    j = 0
    
    for i in range(len(texto_cifrado)):
        char = texto_cifrado[i]
        
        if char.isalpha():
            deslocamento = ord(chave[j % len(chave)]) - ord('a')
            
            if char.isupper():
                resultado += chr((ord(char) - deslocamento - 65 + 26) % 26 + 65)
            else:
                resultado += chr((ord(char) - deslocamento - 97 + 26) % 26 + 97)
            j += 1
        else:
            resultado += char
            
    return resultado
