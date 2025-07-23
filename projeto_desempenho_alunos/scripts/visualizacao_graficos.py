# Projeto criado para fins educacionais por Antunes Menezes,
# com apoio do ChatGPT para estruturação e aprendizado de análise de dados.
# Este script visa facilitar a visualização de desempenho de alunos
# com base em dados simulados do ENEM.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Configurações iniciais
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Carregar os dados
df = pd.read_csv("C:/Analise de Dados/Projetos/projeto_desempenho_alunos/dados/desempenho_simulado.csv")
cortes = pd.read_csv("C:/Analise de Dados/Projetos/projeto_desempenho_alunos/dados/notas_corte_ufpb.csv")
output_path = "C:/Analise de Dados/Projetos/projeto_desempenho_alunos/graficos"

# Gráfico: Média da turma por ano
def grafico_media_turma():
    medias = df.groupby("Ano")["Média"].mean().round(1).reset_index()
    sns.barplot(x="Ano", y="Média", data=medias, palette="Blues_d")
    plt.title("Média da Turma por Ano")
    plt.ylim(0, 800)
    plt.savefig(output_path + "media_turma_por_ano.png")
    plt.show()

# Gráfico: Evolução da média de um aluno
def grafico_evolucao_aluno(nome):
    aluno = df[df["Nome"].str.lower() == nome.lower()]
    if aluno.empty:
        print("Aluno não encontrado.")
        return
    sns.lineplot(x="Ano", y="Média", data=aluno, marker="o")
    plt.title(f"Evolução da Média - {nome}")
    plt.ylim(0, 800)
#    plt.savefig(output_path + f"evolucao_{nome.replace(' ', '_').lower()}.png")
    plt.show()

# Gráfico: Ranking da turma (2024)
def grafico_ranking_2024():
    dados_2024 = df[df["Ano"] == 2024].sort_values("Média", ascending=False)
    sns.barplot(x="Média", y="Nome", data=dados_2024, palette="viridis")
    plt.title("Ranking da Turma - Simulado 2024")
    plt.xlim(0, 800)
#    plt.savefig(output_path + "ranking_2024.png")
    plt.show()

# Gráfico: Comparar média de um aluno com as notas de corte
def grafico_comparativo_cursos(nome):
    aluno = df[(df["Nome"].str.lower() == nome.lower()) & (df["Ano"] == 2024)]
    if aluno.empty:
        print("Aluno não encontrado ou não tem dados de 2024.")
        return
    media_aluno = aluno.iloc[0]["Média"]
    cortes_ = cortes.copy()
    cortes_["Aluno"] = media_aluno

    cursos_plot = cortes_[["Curso", "Nota de Corte", "Aluno"]].melt(id_vars="Curso", var_name="Tipo", value_name="Nota")
    sns.barplot(x="Nota", y="Curso", hue="Tipo", data=cursos_plot, palette="Set2")
    plt.title(f"Comparativo: {nome} x Notas de Corte (2024)")
    plt.xlim(0, 800)
#    plt.savefig(output_path + f"comparativo_cursos_{nome.replace(' ', '_').lower()}.png")
    plt.show()

# Menu de seleção de gráficos
def menu_graficos():
    while True:
        print("\n=== MENU DE GRÁFICOS ===")
        print("1. Média da turma por ano")
        print("2. Evolução da média de um aluno")
        print("3. Ranking da turma (2024)")
        print("4. Comparar média de um aluno com notas de corte")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            grafico_media_turma()
        elif escolha == "2":
            nome = input("Digite o nome do aluno: ")
            grafico_evolucao_aluno(nome)
        elif escolha == "3":
            grafico_ranking_2024()
        elif escolha == "4":
            nome = input("Digite o nome do aluno: ")
            grafico_comparativo_cursos(nome)
        elif escolha == "5":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

# Executar o menu
if __name__ == "__main__":
    menu_graficos()
