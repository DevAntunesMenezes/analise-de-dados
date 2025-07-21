import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar estilo do gráfico
sns.set(style="whitegrid")

# Caminho para o CSV
caminho_arquivo = r'C:\Analise de Dados\Projetos\analise-desempenho-escolar\dados\desempenho_alunos.csv'

# Carregar os dados
df = pd.read_csv(caminho_arquivo)

# Calcular média por aluno (se ainda não foi feito)
colunas_notas = df.columns[2:]
df['Média'] = df[colunas_notas].mean(axis=1)

# Gráfico de barras: média por disciplina 
plt.figure(figsize=(8, 5))
df[colunas_notas].mean().sort_values().plot(kind='bar', color='skyblue')
plt.title('Média Geral por Disciplina')
plt.ylabel('Nota média')
plt.xlabel('Disciplina')
plt.tight_layout()
plt.show()

# Boxplot: distribuição das médias por turma 
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Turma', y='Média', palette='pastel')
plt.title('Distribuição das Médias por Turma')
plt.ylabel('Média dos Alunos')
plt.tight_layout()
plt.show()

# Histograma: distribuição geral das médias 
plt.figure(figsize=(8, 5))
sns.histplot(df['Média'], bins=8, kde=True, color='lightcoral')
plt.title('Distribuição Geral das Médias dos Alunos')
plt.xlabel('Média')
plt.tight_layout()
plt.show()
