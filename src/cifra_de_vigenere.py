def cifra_de_vigenere(texto, chave):
    """
    Cifra de Vigenère: Função que cifra um texto utilizando a cifra de Vigenère.
    
    Parâmetros:
    texto (str): O texto a ser cifrado.
    chave (str): A chave utilizada para cifrar o texto.
    
    Retorna:
    str: O texto cifrado.
    """
    resultado = ""
    chave = chave.lower()
    j = 0
    
    # Percorre cada caractere do texto
    for i in range(len(texto)):
        char = texto[i]
        
        # Verifica se o caractere é uma letra
        if char.isalpha():
            # Determina o deslocamento baseado na chave
            deslocamento = ord(chave[j % len(chave)]) - ord('a')
            
            # Verifica se o caractere é uma letra maiúscula
            if char.isupper():
                resultado += chr((ord(char) + deslocamento - 65) % 26 + 65)
            # Verifica se o caractere é uma letra minúscula
            else:
                resultado += chr((ord(char) + deslocamento - 97) % 26 + 97)
            
            j += 1  # Incrementa o índice da chave
        else:
            resultado += char  # Mantém caracteres não alfabéticos inalterados
    
    return resultado