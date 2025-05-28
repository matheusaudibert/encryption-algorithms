import streamlit as st
from src.cifra_de_cesar import cifra_de_cesar
from src.cifra_de_vigenere import cifra_de_vigenere
from src.decifra_de_cesar import decifra_de_cesar, LETRAS_COMUNS_PT
from src.decifra_de_vigenere import decifra_de_vigenere

st.title("🔑 Algoritmos de Criptografia")

tab_cesar, tab_vigenere, tab_decifrar_cesar, tab_decifra_vigenere = st.tabs(["Cifra de César", "Cifra de Vigenère", "Decifrar Cifra de César", "Decifrar Cifra de Vigenère"])

with tab_cesar:
  st.title("Cifra de César")
  st.write("A cifra de César é uma técnica de criptografia simples e clássica. Ela funciona deslocando cada letra do texto original por um número fixo de posições no alfabeto.")
  
  texto_cesar = st.text_input("Texto a ser cifrado:", placeholder="Digite o texto aqui", key="texto_cifrado_cesar")
  deslocamento = st.number_input("Deslocamento", min_value=0, value=1, key="deslocamento_cesar")
  
  if st.button("Cifrar", key="cifra_de_cesar"):
     texto_cifrado_cesar = cifra_de_cesar(texto_cesar, deslocamento)
     st.write("Texto cifrado:", texto_cifrado_cesar)
  
with tab_vigenere:
  st.title("Cifra de Vigenère")
  st.write("A cifra de Vigenère é uma técnica de criptografia que utiliza uma palavra-chave para cifrar o texto. Cada letra do texto é deslocada por um número de posições determinado pela letra correspondente da chave.")
  
  texto_vigenere = st.text_input("Texto a ser cifrado:", placeholder="Digite o texto aqui", key="texto_cifrado_vigenere")
  chave = st.text_input("Chave:", placeholder="Digite a chave aqui", key="chave_vigenere")
  
  if st.button("Cifrar", key="cifra_de_vigenere"):
     texto_cifrado_vigenere = cifra_de_vigenere(texto_vigenere, chave)
     st.toast("Texto cifrado com sucesso")
     st.write("Texto cifrado:", texto_cifrado_vigenere)
     
with tab_decifrar_cesar:
    st.title("Decifragem da Cifra de César")
    st.write("Tentaremos decifrar o texto usando análise de frequência das letras mais comuns no português.")
    
    texto_cifrado_cesar = st.text_input("Texto a ser decifrado:", placeholder="Digite o texto aqui", key="texto_decifrado_cesar")
    
    if 'current_letter_index' not in st.session_state:
        st.session_state.current_letter_index = 0
        
    if 'resultados' not in st.session_state:
        st.session_state.resultados = None
    
    if st.button("Decifrar", key="decifra_de_cesar"):
        st.session_state.resultados = decifra_de_cesar(texto_cifrado_cesar)
        st.session_state.current_letter_index = 0
        
    if st.session_state.resultados:
        resultado_atual = st.session_state.resultados[st.session_state.current_letter_index]
        
        st.write(f"Tentativa atual: considerando '{resultado_atual['letra_base']}' como letra mais frequente")
        st.write(f"Texto decifrado: {resultado_atual['texto']}")
        
        if st.session_state.current_letter_index < len(LETRAS_COMUNS_PT) - 1:
            if st.button("Próxima tentativa"):
                st.session_state.current_letter_index += 1
                st.rerun()
      
with tab_decifra_vigenere:
    st.title("Decifragem da Cifra de Vigenère")
    st.write("Para decifrar um texto cifrado com Vigenère, você precisa conhecer a chave utilizada.")
    
    texto_cifrado_vigenere = st.text_input("Texto cifrado:", placeholder="Digite o texto cifrado aqui", key="texto_decifrado_vigenere")
    chave_decifragem = st.text_input("Chave de decifragem:", placeholder="Digite a chave aqui", key="chave_decifragem_vigenere")
    
    if st.button("Decifrar", key="decifra_vigenere"):
        if chave_decifragem:
            texto_decifrado = decifra_de_vigenere(texto_cifrado_vigenere, chave_decifragem)
            st.success("Texto decifrado com sucesso!")
            st.write("Texto decifrado:", texto_decifrado)
        else:
            st.error("Por favor, insira uma chave para decifrar o texto.")



