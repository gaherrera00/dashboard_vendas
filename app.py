# 6
# o streamlit tem que rodar aqui
# Configurar página
# Criar sidebar
# Chamar serviços
# Exibir resultados
import streamlit as st
from src.load_data import juntar
from src.filters import criar_filtros, aplicar_filtros

st.set_page_config(page_title="Dashboard de Vendas")

df = juntar()

filtros = criar_filtros(df)
df_filtrado = aplicar_filtros(df, filtros)

st.write(df_filtrado)
