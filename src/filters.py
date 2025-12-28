# 2
# Filtros mínimos aceitáveis
# Categoria (multiselect)
# Produto (dependente da categoria)
# Estado
# Forma de pagamento
# Período (data inicial e final)
import streamlit as st
import pandas as pd


def criar_filtros(df: pd.DataFrame) -> dict:
    st.sidebar.header("Filtros")

    # Categoria
    categorias = st.sidebar.multiselect(
        "Categoria", sorted(df["categoria"].dropna().unique())
    )

    # Produto dependente da categoria
    df_produtos = df.copy()
    if categorias:
        df_produtos = df_produtos[df_produtos["categoria"].isin(categorias)]

    produtos = st.sidebar.multiselect(
        "Produto", sorted(df_produtos["produto"].dropna().unique())
    )

    # Estado
    estados = st.sidebar.multiselect("Estado", sorted(df["estado"].dropna().unique()))

    # Forma de pagamento
    formas_pagamento = st.sidebar.multiselect(
        "Forma de pagamento", sorted(df["forma_pagamento"].dropna().unique())
    )

    # Período
    data_min = df["data"].min()
    data_max = df["data"].max()

    data_inicio, data_fim = st.sidebar.date_input(
        "Período", value=(data_min, data_max), min_value=data_min, max_value=data_max
    )

    return {
        "categorias": categorias,
        "produtos": produtos,
        "estados": estados,
        "formas_pagamento": formas_pagamento,
        "data_inicio": data_inicio,
        "data_fim": data_fim,
    }


def aplicar_filtros(df: pd.DataFrame, filtros: dict) -> pd.DataFrame:
    df_f = df.copy()

    if filtros["categorias"]:
        df_f = df_f[df_f["categoria"].isin(filtros["categorias"])]

    if filtros["produtos"]:
        df_f = df_f[df_f["produto"].isin(filtros["produtos"])]

    if filtros["estados"]:
        df_f = df_f[df_f["estado"].isin(filtros["estados"])]

    if filtros["formas_pagamento"]:
        df_f = df_f[df_f["forma_pagamento"].isin(filtros["formas_pagamento"])]

    data_inicio = pd.to_datetime(filtros["data_inicio"])
    data_fim = pd.to_datetime(filtros["data_fim"])

    df_f = df_f[df_f["data"].between(data_inicio, data_fim)]

    return df_f
