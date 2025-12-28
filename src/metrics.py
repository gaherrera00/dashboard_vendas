# 3
# Receita total
# Lucro total
# Margem média
# Ticket médio
# Nº de pedidos
# Produto mais lucrativo
# Categoria mais lucrativa
# Estado com maior faturamento
# Crescimento mês a mês (%)
# Receita período atual vs anterior
# Top 20% produtos que geram 80% da receita


import pandas as pd


def calcular_metricas(df_filtrado: pd.DataFrame, df_completo: pd.DataFrame) -> dict:
    receita_total = df_filtrado["receita"].sum()
    lucro_total = df_filtrado["lucro"].sum()

    num_pedidos = df_filtrado["pedido_id"].nunique()
    ticket_medio = receita_total / num_pedidos if num_pedidos > 0 else 0

    margem_media = (lucro_total / receita_total) * 100 if receita_total > 0 else 0

    produto_lucrativo = (
        df_filtrado.groupby("produto", observed=True)["lucro"].sum().idxmax()
        if not df_filtrado.empty
        else None
    )

    categoria_lucrativa = (
        df_filtrado.groupby("categoria", observed=True)["lucro"].sum().idxmax()
        if not df_filtrado.empty
        else None
    )

    estado_top = (
        df_filtrado.groupby("estado", observed=True)["receita"].sum().idxmax()
        if not df_filtrado.empty
        else None
    )

    # comparação período
    data_ini = df_filtrado["data"].min()
    data_fim = df_filtrado["data"].max()
    dias = (data_fim - data_ini).days + 1

    periodo_ant_ini = data_ini - pd.Timedelta(days=dias)
    periodo_ant_fim = data_ini - pd.Timedelta(days=1)

    receita_atual = receita_total

    receita_anterior = df_completo.query(
        "data >= @periodo_ant_ini and data <= @periodo_ant_fim"
    )["receita"].sum()

    variacao_periodo = (
        (receita_atual - receita_anterior) / receita_anterior * 100
        if receita_anterior > 0
        else None
    )

    return {
        "receita_total": receita_total,
        "lucro_total": lucro_total,
        "margem_media": margem_media,
        "ticket_medio": ticket_medio,
        "num_pedidos": num_pedidos,
        "produto_lucrativo": produto_lucrativo,
        "categoria_lucrativa": categoria_lucrativa,
        "estado_top": estado_top,
        "variacao_periodo": variacao_periodo,
    }
