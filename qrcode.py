# IMPORTANDO AS BIBLIOTECAS:
import pyqrcode
import png
from pyqrcode import QRCode
import streamlit as st

# TÍTULO DASHBOARD:
st.title(':green[QRCODE]')


# INPUT DO LINK DO QUAL SERÁ GERADO O QRCODE: 
input_link = st.text_input('Digite ou cole o link da página que deseja gerar o QRCODE: ')


# INPUT DO NOME DA IMAGEM DO QRCODE:
input_nome_imagem = st.text_input('Digite o nome do arquivo a ser gerado: ')


# GERANDO O URL DO QRCODE:
url = pyqrcode.create(input_link)


# GERANDO A IMAGEM DO QRCODE:
imagem = url.png(f'{input_nome_imagem}.png', scale=8)


with st.container():
    st.image(f'{input_nome_imagem}.png')















