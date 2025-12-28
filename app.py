import streamlit as st
import pandas as pd

from src.load_data import juntar
from src.filters import criar_filtros, aplicar_filtros
from src.metrics import calcular_metricas
from src.charts import (
    receita_por_categoria,
    receita_no_tempo,
    lucro_por_categoria,
    top_10_produtos,
    distribuicao_pagamento,
    receita_por_estado,
)

# Configuração da página
st.set_page_config(
    page_title="Dashboard de Vendas",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Estilo mínimo (sem excesso visual)
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# Carregamento de dados
@st.cache_data(show_spinner=False)
def carregar_dados():
    return juntar()


df_completo, linhas_descartadas = carregar_dados()

# Sidebar — filtros
with st.sidebar:
    st.header("Filtros")
    filtros = criar_filtros(df_completo)

# Aplicação de filtros
df_filtrado = aplicar_filtros(df_completo, filtros)

if df_filtrado.empty:
    st.warning("Nenhum dado encontrado para os filtros selecionados.")
    st.stop()

# Cabeçalho
st.title("Dashboard de Vendas")

if linhas_descartadas > 0:
    st.caption(f"{linhas_descartadas} registros foram descartados por inconsistência.")

st.divider()

# Métricas
metricas = calcular_metricas(df_filtrado, df_completo)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Receita Total",
    f"R$ {metricas['receita_total']:,.2f}",
    f"{metricas['variacao_periodo']:.1f}%" if metricas["variacao_periodo"] else None,
)

col2.metric("Lucro Total", f"R$ {metricas['lucro_total']:,.2f}")
col3.metric("Margem Média", f"{metricas['margem_media']:.1f}%")
col4.metric("Ticket Médio", f"R$ {metricas['ticket_medio']:,.2f}")
col5.metric("Número de Pedidos", f"{metricas['num_pedidos']:,}")

st.divider()

# Destaques
col1, col2, col3 = st.columns(3)

col1.write("**Produto mais lucrativo**")
col1.write(metricas["produto_lucrativo"])

col2.write("**Categoria mais lucrativa**")
col2.write(metricas["categoria_lucrativa"])

col3.write("**Estado com maior faturamento**")
col3.write(metricas["estado_top"])

st.divider()

# Gráficos
st.subheader("Análises")

col1, col2 = st.columns(2)
col1.plotly_chart(receita_por_categoria(df_filtrado), use_container_width=True)
col2.plotly_chart(receita_no_tempo(df_filtrado), use_container_width=True)

col1, col2 = st.columns(2)
col1.plotly_chart(lucro_por_categoria(df_filtrado), use_container_width=True)
col2.plotly_chart(top_10_produtos(df_filtrado), use_container_width=True)

col1, col2 = st.columns(2)
col1.plotly_chart(distribuicao_pagamento(df_filtrado), use_container_width=True)
col2.plotly_chart(receita_por_estado(df_filtrado), use_container_width=True)

st.divider()

# Tabela detalhada
st.subheader("Dados Detalhados")

df_exibicao = df_filtrado.copy()

colunas_monetarias = [
    "preco_unitario",
    "custo_unitario",
    "receita",
    "custo_total",
    "lucro",
]

for col in colunas_monetarias:
    df_exibicao[col] = df_exibicao[col].map(lambda x: f"R$ {x:,.2f}")

df_exibicao["margem_lucro"] = df_exibicao["margem_lucro"].map(lambda x: f"{x:.1f}%")

ordem_colunas = [
    "data",
    "pedido_id",
    "cliente_id",
    "produto",
    "categoria",
    "preco_unitario",
    "quantidade",
    "receita",
    "custo_total",
    "lucro",
    "margem_lucro",
    "forma_pagamento",
    "estado",
]

df_exibicao = df_exibicao[ordem_colunas]

with st.expander("Visualizar dados"):
    st.dataframe(
        df_exibicao,
        use_container_width=True,
        hide_index=True,
        height=400,
    )

    csv = df_filtrado.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Download CSV",
        csv,
        "vendas_filtradas.csv",
        "text/csv",
    )

# Rodapé
st.caption("Dashboard de Vendas • Streamlit + Plotly")
