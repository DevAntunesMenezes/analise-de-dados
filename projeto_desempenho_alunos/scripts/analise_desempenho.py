# Projeto criado para fins educacionais por Antunes Menezes,
# com apoio do ChatGPT para estruturação e aprendizado de análise de dados.
# Este script visa facilitar a visualização de desempenho de alunos
# com base em dados simulados do ENEM.

import pandas as pd

# Carregar dados
# df = pd.read_csv("dados/desempenho_simulado.csv")
# cortes = pd.read_csv("dados/notas_corte_ufpb.csv")
df = pd.read_csv("C:/Analise de Dados/Projetos/projeto_desempenho_alunos/dados/desempenho_simulado.csv")
cortes = pd.read_csv("C:/Analise de Dados/Projetos/projeto_desempenho_alunos/dados/notas_corte_ufpb.csv")

# Funções
def media_turma_por_ano():
    medias = df.groupby("Ano")["Média"].mean().round(1)
    print("\nMédia da turma por ano:")
    print(medias)

def evolucao_aluno(nome):
    aluno = df[df["Nome"].str.lower() == nome.lower()]
    if aluno.empty:
        print("Aluno não encontrado.")
    else:
        print(f"\nNotas de {nome}:")
        print(aluno[["Ano", "CN", "CH", "LC", "MT", "Redação", "Média"]])

def cursos_alcancaveis(nome):
    aluno = df[(df["Nome"].str.lower() == nome.lower()) & (df["Ano"] == 2024)]
    if aluno.empty:
        print("Aluno não encontrado ou não tem dados de 2024.")
        return
    media_final = aluno.iloc[0]["Média"]
    print(f"\nMédia final de {nome} em 2024: {media_final}")
    possiveis = cortes[cortes["Nota de Corte"] <= media_final]
    if possiveis.empty:
        print("Nenhum curso alcançado com essa média.")
    else:
        print("Cursos que poderiam ser alcançados:")
        print(possiveis[["Curso", "Universidade", "Nota de Corte"]])

# Menu interativo
def menu():
    while True:
        print("\n=== MENU DE ANÁLISE ===")
        print("1. Ver média da turma por ano")
        print("2. Ver evolução de um aluno")
        print("3. Ver cursos possíveis para um aluno (com base em 2024)")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            media_turma_por_ano()
        elif opcao == "2":
            nome = input("Digite o nome do aluno: ")
            evolucao_aluno(nome)
        elif opcao == "3":
            nome = input("Digite o nome do aluno: ")
            cursos_alcancaveis(nome)
        elif opcao == "4":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

# Executar menu
if __name__ == "__main__":
    menu()
