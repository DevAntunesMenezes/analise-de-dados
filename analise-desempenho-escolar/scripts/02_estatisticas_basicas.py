import pandas as pd

# Caminho para o CSV (mesmo da etapa anterior)
caminho_arquivo = r'C:\Analise de Dados\Projetos\analise-desempenho-escolar\dados\desempenho_alunos.csv'

# Carregar os dados
df = pd.read_csv(caminho_arquivo)

# Exibir estatísticas descritivas das colunas numéricas
print("Estatísticas descritivas das notas:")
print(df.describe())

# Verificar se há valores ausentes (nulos)
# print("\nHá valores ausentes no arquivo?")
# print(df.isnull().sum())
