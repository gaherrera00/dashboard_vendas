# 4
# # Gráficos essenciais
# Receita por categoria (barras)
# Receita no tempo (linha)
# Lucro por categoria
# Top 10 produtos
# Distribuição por forma de pagamento
# Receita por estado (mapa ou barras)

# Regras
# Título claro
# Unidade explícita (R$)
# Nada poluído
# Retornar o gráfico pronto
import plotly.express as px
import pandas as pd


# Receita por categoria (barras)
def receita_por_categoria(df: pd.DataFrame):
    dados = (
        df.groupby("categoria", observed=True, as_index=False)["receita"]
        .sum()
        .sort_values("receita", ascending=False)
    )

    fig = px.bar(
        dados,
        x="categoria",
        y="receita",
        title="Receita por Categoria",
        labels={"receita": "Receita (R$)", "categoria": "Categoria"},
    )

    fig.update_layout(xaxis_tickangle=-45)
    return fig


# Receita no tempo (linha)
def receita_no_tempo(df: pd.DataFrame):
    dados = df.set_index("data").resample("M")["receita"].sum().reset_index()

    fig = px.line(
        dados,
        x="data",
        y="receita",
        title="Receita ao Longo do Tempo",
        labels={"receita": "Receita (R$)", "data": "Período"},
    )

    return fig


# Lucro por categoria (barras)
def lucro_por_categoria(df: pd.DataFrame):
    dados = (
        df.groupby("categoria", observed=True, as_index=False)["lucro"]
        .sum()
        .sort_values("lucro", ascending=False)
    )

    fig = px.bar(
        dados,
        x="categoria",
        y="lucro",
        title="Lucro por Categoria",
        labels={"lucro": "Lucro (R$)", "categoria": "Categoria"},
    )

    fig.update_layout(xaxis_tickangle=-45)
    return fig


# Top 10 produtos por receita (barras horizontais)
def top_10_produtos(df: pd.DataFrame):
    dados = (
        df.groupby("produto", observed=True, as_index=False)["receita"]
        .sum()
        .sort_values("receita", ascending=False)
        .head(10)
        .sort_values("receita")
    )

    fig = px.bar(
        dados,
        x="receita",
        y="produto",
        orientation="h",
        title="Top 10 Produtos por Receita",
        labels={"receita": "Receita (R$)", "produto": "Produto"},
    )

    return fig


# Distribuição por forma de pagamento (pizza)
def distribuicao_pagamento(df: pd.DataFrame):
    dados = df.groupby("forma_pagamento", observed=True, as_index=False)[
        "receita"
    ].sum()

    fig = px.pie(
        dados,
        names="forma_pagamento",
        values="receita",
        title="Distribuição da Receita por Forma de Pagamento",
        hole=0.4,  # donut discreto
    )

    return fig


# Receita por estado (barras)
def receita_por_estado(df: pd.DataFrame):
    dados = (
        df.groupby("estado", observed=True, as_index=False)["receita"]
        .sum()
        .sort_values("receita", ascending=False)
    )

    fig = px.bar(
        dados,
        x="estado",
        y="receita",
        title="Receita por Estado",
        labels={"receita": "Receita (R$)", "estado": "Estado"},
    )

    return fig
