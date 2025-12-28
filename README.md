# 📊 Dashboard de Vendas E-commerce

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Plotly](https://img.shields.io/badge/Plotly-5.17+-purple.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**Dashboard interativo para análise de vendas de e-commerce com visualizações em tempo real**

[🚀 Demo](#demo) • [📦 Instalação](#instalação) • [🎯 Funcionalidades](#funcionalidades) • [📈 Capturas](#capturas-de-tela) • [🤝 Contribuindo](#contribuindo)

</div>

---

## 🎯 Sobre o Projeto

Dashboard analítico desenvolvido em Python com Streamlit para visualização e análise de dados de vendas de e-commerce. O sistema oferece insights em tempo real sobre receita, lucro, produtos, categorias e comportamento de vendas por região.

### 🎓 Objetivo

Este projeto foi desenvolvido como parte do aprendizado de análise de dados e visualização, demonstrando habilidades em:

- Manipulação de dados com Pandas
- Criação de dashboards interativos com Streamlit
- Visualizações avançadas com Plotly
- Engenharia de features e métricas de negócio
- Boas práticas de organização de código Python

---

## ✨ Funcionalidades

### 📊 Indicadores Principais (KPIs)

- **Receita Total** com comparação período anterior
- **Lucro Total** e margem de lucro média
- **Ticket Médio** por pedido
- **Número de Pedidos** processados
- **Variação Percentual** entre períodos

### 🏆 Análises de Destaque

- Produto mais lucrativo
- Categoria com melhor desempenho
- Estado com maior faturamento

### 📈 Visualizações Interativas

1. **Receita por Categoria** - Gráfico de barras
2. **Receita ao Longo do Tempo** - Série temporal
3. **Lucro por Categoria** - Análise de rentabilidade
4. **Top 10 Produtos** - Ranking por receita
5. **Distribuição por Forma de Pagamento** - Gráfico de pizza
6. **Receita por Estado** - Análise geográfica

### 🔍 Filtros Avançados

- **Categoria** - Seleção múltipla
- **Produto** - Filtro dependente da categoria
- **Estado** - Análise regional
- **Forma de Pagamento** - Crédito, Débito, Pix, Boleto
- **Período** - Intervalo de datas customizável

### 📋 Recursos Adicionais

- Visualização de dados brutos formatados
- Download de dados filtrados em CSV
- Contador de registros exibidos
- Validação automática de dados
- Cache para otimização de performance

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia                                                                                            | Versão | Uso                       |
| ----------------------------------------------------------------------------------------------------- | ------ | ------------------------- |
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)          | 3.8+   | Linguagem principal       |
| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) | 1.28+  | Framework web             |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)          | 2.0+   | Manipulação de dados      |
| ![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=plotly&logoColor=white)          | 5.17+  | Visualizações interativas |

---

## 📦 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone o repositório**

```bash
git clone https://github.com/gaherrera00/dashboard_vendas.git
cd dashboard-vendas-ecommerce
```

2. **Crie um ambiente virtual (recomendado)**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Instale as dependências**

```bash
pip install -r requirements.txt
```

4. **Execute o dashboard**

```bash
streamlit run app.py
```

5. **Acesse no navegador**

```
http://localhost:8501
```

---

## 📂 Estrutura do Projeto

```
dashboard-vendas-ecommerce/
│
├── app.py                      # Aplicação principal Streamlit
├── requirements.txt            # Dependências do projeto
├── .gitignore                 # Arquivos ignorados pelo Git
├── README.md                  # Documentação
│
├── data/
│   └── vendas_ecommerce.csv   # Dataset de vendas
│
└── src/
    ├── __init__.py
    ├── load_data.py           # Carregamento e validação de dados
    ├── filters.py             # Lógica de filtros
    ├── metrics.py             # Cálculo de métricas
    └── charts.py              # Criação de gráficos
```

## 📊 Dataset

O dataset utilizado contém informações de vendas de e-commerce com as seguintes colunas:

| Coluna            | Tipo     | Descrição                     |
| ----------------- | -------- | ----------------------------- |
| `data`            | Date     | Data da transação             |
| `pedido_id`       | String   | Identificador único do pedido |
| `cliente_id`      | String   | Identificador do cliente      |
| `produto`         | Category | Nome do produto               |
| `categoria`       | Category | Categoria do produto          |
| `preco_unitario`  | Float    | Preço unitário do produto     |
| `quantidade`      | Integer  | Quantidade vendida            |
| `custo_unitario`  | Float    | Custo unitário do produto     |
| `forma_pagamento` | Category | Método de pagamento           |
| `estado`          | Category | Estado da transação           |

### Colunas Calculadas

- **receita**: `preco_unitario × quantidade`
- **custo_total**: `custo_unitario × quantidade`
- **lucro**: `receita - custo_total`
- **margem_lucro**: `(lucro / receita) × 100`

---

## 🔧 Validações Implementadas

O sistema realiza validações automáticas para garantir a integridade dos dados:

- ✅ Preço unitário deve ser maior que zero
- ✅ Custo unitário deve ser menor que preço unitário
- ✅ Quantidade deve ser maior ou igual a 1
- ✅ Data deve estar entre 2020-01-01 e 2025-12-31
- ✅ Remoção automática de registros inválidos com contabilização

---

## 🚀 Funcionalidades Futuras

- [ ] Análise preditiva de vendas
- [ ] Segmentação de clientes (RFM)
- [ ] Análise de cesta de produtos
- [ ] Dashboard em tempo real com atualização automática
- [ ] Exportação de relatórios em PDF
- [ ] Integração com APIs de e-commerce
- [ ] Sistema de alertas para métricas críticas
- [ ] Análise de sazonalidade avançada

## 👤 Autor

**Gabriel Herrera Demarchi**

- GitHub: [GitHub](https://github.com/gaherrera00)
- LinkedIn: [LinkedIn](https://www.linkedin.com/in/gabriel-herrera-demarchi-532844338/)
- Email: gabriel.h.demarchi@gmail.com
