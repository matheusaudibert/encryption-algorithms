def cifra_de_cesar(texto, deslocamento):
    """
    Cifra de César: Função que cifra um texto utilizando a cifra de César.
    
    Parâmetros:
    texto (str): O texto a ser cifrado.
    deslocamento (int): O número de posições que cada letra deve ser deslocada.
    
    Retorna:
    str: O texto cifrado.
    """
    resultado = ""
    
    # Percorre cada caractere do texto
    for i in range(len(texto)):
        char = texto[i]
        
        # Verifica se o caractere é uma letra maiúscula
        if char.isupper():
            resultado += chr((ord(char) + deslocamento - 65) % 26 + 65)
        # Verifica se o caractere é uma letra minúscula
        elif char.islower():
            resultado += chr((ord(char) + deslocamento - 97) % 26 + 97)
        else:
            resultado += char
    
    return resultado