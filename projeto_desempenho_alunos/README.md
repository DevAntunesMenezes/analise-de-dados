
# 📊 Projeto de Análise de Desempenho dos Alunos (Simulados ENEM)

Este projeto tem como objetivo analisar o desempenho de uma turma de alunos ao longo de três anos (2022, 2023 e 2024) com base em dados simulados do ENEM, utilizando Python. O projeto permite explorar os dados por meio de um menu interativo e também gerar visualizações gráficas para melhor apresentação.

---

## Funcionalidades do Projeto

### `analise_desempenho.py`
Menu interativo com as seguintes opções:

1. Ver média da turma por ano
2. Ver evolução de um aluno
3. Ver cursos possíveis para um aluno (baseado na média de 2024)
4. Sair do programa

### `visualizacao_graficos.py` (versão 1)
Menu gráfico com opções de visualização individual:

1. Média da turma por ano (barras)
2. Evolução da média de um aluno (linha)
3. Ranking da turma (2024)
4. Comparativo entre a média do aluno e notas de corte (colunas lado a lado)

### `visualizacao_graficos_v2.py` (versão 2)
Menu com gráficos mais amplos e comparativos:

1. Evolução da média de todos os alunos nos três anos (linhas)
2. Médias dos alunos em 2024 com linha de nota de corte média (barra + linha vermelha)

---

## ▶️ Como Executar

1. Baixe o projeto e abra no seu ambiente Python (recomendado: **Spyder**).
2. Certifique-se de que os arquivos `.csv` estão dentro da pasta `dados/`.
3. Execute o script desejado dentro da pasta `scripts/`.
4. Utilize o menu no terminal para interagir com as análises ou gerar gráficos.

---

## Exemplos de Análises e Visualizações

- Evolução da média de cada aluno ao longo dos anos.
- Comparação entre a média da turma nos simulados.
- Simulação de cursos que o aluno pode alcançar com a média de 2024.
- Ranking de desempenho dos alunos.
- Gráficos comparativos para apresentações ou relatórios.
- Visualização da média geral da turma em relação às notas de corte dos cursos da UFPB.

---

## Tecnologias Utilizadas

- Python 3
- pandas
- matplotlib
- seaborn
- Ambiente Spyder (Anaconda)

---

## 🧑‍💻 Autor

Projeto educacional desenvolvido por **Antunes Menezes**, como prática de Python para análise de dados e visualização de desempenho escolar.

Este projeto foi realizado com o apoio do **ChatGPT**, que ajudou a orientar a estrutura, revisar e comentar os códigos passo a passo, com explicações voltadas ao aprendizado e à boa organização dos dados.
