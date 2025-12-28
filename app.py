# o streamlit tem que rodar aqui
# Configurar página
# Criar sidebar
# Chamar serviços
# Exibir resultados
from src.load_data import juntar

df = juntar()
print(df.head())
