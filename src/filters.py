# 2
# Filtros mínimos aceitáveis
# Categoria (multiselect)
# Produto (dependente da categoria)
# Estado
# Forma de pagamento
# Período (data inicial e final)
import streamlit as st


# def criar_filtros(df):
#     st.sidebar.title("Filtros")
#     st.sidebar.write("Selecione as opções")

#     st.sidebar.caption("Categorias")
#     categorias = st.sidebar.multiselect("Categorias", df["categoria"].unique())
#     if categorias:
#         df = df[df["categoria"].isin(categorias)]

import streamlit as st


def criar_filtros(df):
    st.sidebar.header("Filtros")

    categorias = st.sidebar.multiselect("Categoria", sorted(df["categoria"].unique()))

    if "filtros" not in st.session_state:
        st.session_state["filtros"] = {}

    if st.sidebar.button("Aplicar filtros"):
        st.session_state["filtros"] = {"categorias": categorias}

    return st.session_state["filtros"]


def aplicar_filtros(df, filtros):
    df_f = df.copy()

    if filtros.get("categorias"):
        df_f = df_f[df_f["categoria"].isin(filtros["categorias"])]

    return df_f
