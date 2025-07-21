import pandas as pd

# Caminho para o CSV
caminho_arquivo = r'C:\Analise de Dados\Projetos\analise-desempenho-escolar\dados\desempenho_alunos.csv'

# Carregar os dados
df = pd.read_csv(caminho_arquivo)

# Selecionar apenas as colunas de nota (do índice 2 até o final)
colunas_notas = df.columns[2:]  # Ignora Aluno e Turma

# Calcular a média por aluno e adicionar uma nova coluna
df['Média'] = df[colunas_notas].mean(axis=1)

# Mostrar os 10 alunos com melhor desempenho
print("Top 10 alunos com maior média:")
print(df[['Aluno', 'Turma', 'Média']].sort_values(by='Média', ascending=False).head(10))

# Mostrar os 10 alunos com menor média
print("\nAlunos com menor desempenho:")
print(df[['Aluno', 'Turma', 'Média']].sort_values(by='Média').head(10))

# Mostrar estatísticas da nova coluna de média
print("\nEstatísticas da média dos alunos:")
print(df['Média'].describe())
