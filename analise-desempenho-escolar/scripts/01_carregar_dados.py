import pandas as pd

# Caminho - escolha uma das opções abaixo:
caminho_arquivo = r'C:\Analise de Dados\Projetos\analise-desempenho-escolar\dados\desempenho_alunos.csv'
# ou
# caminho_arquivo = 'C:/Analise de Dados/Projetos/analise-desempenho-escolar/dados/desempenho_alunos.csv'

df = pd.read_csv(caminho_arquivo)

print("Visualização inicial dos dados:")
print(df.head())

# print("\nColunas disponíveis:")
# print(df.columns)

