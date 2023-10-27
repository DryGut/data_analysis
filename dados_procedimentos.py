import pandas as pd
import matplotlib.pyplot as plt
import re

pd.set_option(
    "display.max_rows", 1000, "display.min_rows", 200,
    "display.max_columns", None, "display.width", None)

df = pd.read_csv('atendimentos_2021_outros.csv')

procedimentos_tratados = []
procedimentos = df['Procedimentos'].str.replace(r'\d+ \-', '', regex=True).fillna('Linha vazia')

for procedimento in procedimentos:
    dados = procedimento.split(',')
    if len(dados) >= 2:
        for dado in dados:
            procedimentos_tratados.append(dado.strip())
            continue
    elif len(dados) <= 1:
        string = ''.join(dados)
        procedimentos_tratados.append(string.strip())

for linhas in procedimentos_tratados:
    if linhas == 'Linha vazia':
        procedimentos_tratados.remove(linhas)

dados_para_uso = pd.DataFrame(procedimentos_tratados)
dados_para_uso.value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribuição dos Procedimentos por Tipos')
plt.axis('equal')
plt.show()
