
# Projeto criado para fins educacionais por Antunes Menezes,
# com apoio do ChatGPT para estruturação e aprendizado de análise de dados.
# Este script visa facilitar a visualização coletiva de desempenho de alunos
# com base em dados simulados do ENEM, incluindo comparações com notas de corte.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configurações de estilo
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 7)

# Caminhos dos dados (ajuste se necessário)
df = pd.read_csv("C:/Analise de Dados/Projetos/projeto_desempenho_alunos/dados/desempenho_simulado.csv")
cortes = pd.read_csv("C:/Analise de Dados/Projetos/projeto_desempenho_alunos/dados/notas_corte_ufpb.csv")

# Gráfico 1: Evolução geral da turma (média por aluno nos 3 anos)
def grafico_evolucao_geral_turma():
    pivot = df.pivot_table(index="Ano", columns="Nome", values="Média")
    pivot.plot(marker="o")
    plt.title("Evolução da Média dos Alunos (2022–2024)")
    plt.xlabel("Ano")
    plt.ylabel("Média ENEM")
    plt.ylim(0, 800)
    plt.legend(loc="upper left", bbox_to_anchor=(1.0, 1.0))
    plt.tight_layout()
    plt.show()

# Gráfico 2: Médias de 2024 com linha de nota de corte
def grafico_media_2024_com_corte():
    dados_2024 = df[df["Ano"] == 2024].sort_values("Média", ascending=False)
    corte_referencia = cortes["Nota de Corte"].mean().round(1)

    sns.barplot(x="Nome", y="Média", data=dados_2024, palette="coolwarm")
    plt.axhline(corte_referencia, color="red", linestyle="--", label=f"Média de corte ({corte_referencia})")
    plt.title("Média dos Alunos em 2024 vs Nota de Corte Média")
    plt.xlabel("Aluno")
    plt.ylabel("Média ENEM")
    plt.xticks(rotation=45, ha="right")
    plt.ylim(0, 800)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Menu gráfico versão 2
def menu_graficos_v2():
    while True:
        print("\n=== MENU DE GRÁFICOS V2 ===")
        print("1. Evolução da média de todos os alunos (2022–2024)")
        print("2. Médias dos alunos em 2024 com linha de nota de corte")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            grafico_evolucao_geral_turma()
        elif escolha == "2":
            grafico_media_2024_com_corte()
        elif escolha == "3":
            print("Encerrando versão 2...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu_graficos_v2()
