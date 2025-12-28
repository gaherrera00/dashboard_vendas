# 1
# leitura e validacao
# Leitura do CSV
# Tipagem correta
# Criação de colunas derivadas
# Remoção de dados inválidos

# Colunas que você DEVE criar
# receita
# custo_total
# lucro
# margem_lucro (%)

# Validações obrigatórias
# preço <= 0 → inválido
# custo >= preço → inválido
# quantidade < 1 → inválido
# data fora do intervalo → inválido
# Você precisa contar e registrar quantas linhas foram descartadas.
import pandas as pd

DATA_MIN = pd.to_datetime("2020-01-01")
DATA_MAX = pd.to_datetime("2025-12-31")


def ler_csv():
    return pd.read_csv("data/vendas_ecommerce.csv")


def tipagem(df):
    df["data"] = pd.to_datetime(df["data"], errors="coerce")

    df["pedido_id"] = df["pedido_id"].astype("string")
    df["cliente_id"] = df["cliente_id"].astype("string")

    categoricas = ["produto", "categoria", "forma_pagamento", "estado"]
    df[categoricas] = df[categoricas].astype("category")

    return df


def criar_colunas(df):
    df["receita"] = df["preco_unitario"] * df["quantidade"]
    df["custo_total"] = df["custo_unitario"] * df["quantidade"]
    df["lucro"] = df["receita"] - df["custo_total"]

    df["margem_lucro"] = (df["lucro"] / df["receita"]) * 100

    return df


def validar(df):
    antes = len(df)

    df = df[
        (df["preco_unitario"] > 0)
        & (df["custo_unitario"] < df["preco_unitario"])
        & (df["quantidade"] >= 1)
        & (df["data"].between(DATA_MIN, DATA_MAX))
    ]

    descartadas = antes - len(df)
    print(f"\n----- Linhas Descatadas: {descartadas} -----\n")

    return df, descartadas


def juntar():
    df = ler_csv()
    df = tipagem(df)
    df = criar_colunas(df)
    df, descartadas = validar(df)

    return df, descartadas
