from collections import Counter

LETRAS_COMUNS_PT = ['A', 'E', 'O', 'S', 'R'] 

def analisar_frequencia(texto):
    letras = [c.upper() for c in texto if c.isalpha()]
    return Counter(letras)

def aplicar_cesar(texto, deslocamento):
    resultado = ""
    for c in texto:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            nova_letra = chr((ord(c) - base - deslocamento) % 26 + base)
            resultado += nova_letra
        else:
            resultado += c
    return resultado

def decifra_de_cesar(texto):
    frequencia = analisar_frequencia(texto)
    letra_mais_comum = frequencia.most_common(1)[0][0]
    
    resultados = []
    
    for letra_ref in LETRAS_COMUNS_PT:
        deslocamento = (ord(letra_mais_comum) - ord(letra_ref)) % 26
        texto_decifrado = aplicar_cesar(texto, deslocamento)
        resultados.append({
            'deslocamento': deslocamento,
            'texto': texto_decifrado,
            'letra_base': letra_ref
        })
    
    return resultados