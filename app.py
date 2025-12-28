# 6
# o streamlit tem que rodar aqui
# Configurar página
# Criar sidebar
# Chamar serviços
# Exibir resultados
import streamlit as st

st.set_page_config(page_title="Dashboard de Vendas", layout="wide")

from src.load_data import juntar
from src.filters import criar_filtros, aplicar_filtros
from src.charts import (
    receita_por_categoria,
    receita_no_tempo,
    lucro_por_categoria,
    top_10_produtos,
    distribuicao_pagamento,
    receita_por_estado,
)

df, descartadas = juntar()
filtros = criar_filtros(df)
df_filtrado = aplicar_filtros(df, filtros)

st.dataframe(df_filtrado, use_container_width=True, hide_index=True)

st.plotly_chart(receita_por_categoria(df_filtrado), use_container_width=True)
st.plotly_chart(receita_no_tempo(df_filtrado), use_container_width=True)
st.plotly_chart(lucro_por_categoria(df_filtrado), use_container_width=True)
st.plotly_chart(top_10_produtos(df_filtrado), use_container_width=True)
st.plotly_chart(distribuicao_pagamento(df_filtrado), use_container_width=True)
st.plotly_chart(receita_por_estado(df_filtrado), use_container_width=True)
