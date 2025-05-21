import streamlit as st
from src.cifra_de_cesar import cifra_de_cesar
from src.cifra_de_vigenere import cifra_de_vigenere

st.title("🔑 Algoritmos de Criptografia")

tab_cesar, tab_vigenere, tab_frequencia_vigenere = st.tabs(["Cifra de César", "Cifra de Vigenère", "Análise de Frequência com Vigenère"])

with tab_cesar:
  st.title("Cifra de César")
  st.write("A cifra de César é uma técnica de criptografia simples e clássica. Ela funciona deslocando cada letra do texto original por um número fixo de posições no alfabeto.")
  
  texto = st.text_input("Texto a ser cifrado:", placeholder="Digite o texto aqui", key="texto_cesar")
  deslocamento = st.number_input("Deslocamento", min_value=0, value=1, key="deslocamento_cesar")
  
  if st.button("Cifrar", key="cifra_de_cesar"):
     texto_cifrado = cifra_de_cesar(texto, deslocamento)
     st.write("Texto cifrado:", texto_cifrado)
    
with tab_vigenere:
  st.title("Cifra de Vigenère")
  st.write("A cifra de Vigenère é uma técnica de criptografia que utiliza uma palavra-chave para cifrar o texto. Cada letra do texto é deslocada por um número de posições determinado pela letra correspondente da chave.")
  
  texto_vigenere = st.text_input("Texto a ser cifrado:", placeholder="Digite o texto aqui", key="texto_vigenere")
  chave = st.text_input("Chave:", placeholder="Digite a chave aqui", key="chave_vigenere")
  
  if st.button("Cifrar", key="cifra_de_vigenere"):
     texto_cifrado_vigenere = cifra_de_vigenere(texto_vigenere, chave)
     st.write("Texto cifrado:", texto_cifrado_vigenere)
    
with tab_frequencia_vigenere:
  
  
  