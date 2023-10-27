import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option(
    "display.max_rows", 1000, "display.min_rows", 200,
    "display.max_columns", None, "display.width", None)

df = pd.read_csv('atendimentos_2021_outros.csv')

""" 
Coletando e criando as lista dos dados a serem trabalhados 
"""
especialidades = df.groupby('Especialidade')
genero = df.groupby('Sexo')
especialidades_tratadas = []
generos = []

""" Definindo algumas funções para tratar os dados"""
def inserindo_dados(dados, lista):
    for nome, grupo in dados:
        lista.append(nome)
        lista.append(len(grupo))

def Convert(lista):
    dados = iter(lista)
    dicionario = dict(zip(dados, dados))
    return dicionario

def coletando_dados_para_grafico(dados, etiqueta, tamanho):
    for k, v in Convert(dados).items():
        etiqueta.append(k)
        tamanho.append(v)

""" Dados sendo tratados para uso nos graficos """
inserindo_dados(genero, generos)
inserindo_dados(especialidades, especialidades_tratadas)

labels_especialidade = []
sizes_especialidade = []
labels_generos = []
sizes_genero = []

coletando_dados_para_grafico(especialidades_tratadas, labels_especialidade, sizes_especialidade)
coletando_dados_para_grafico(generos, labels_generos, sizes_genero)

pos = np.arange(len(labels_especialidade))
tamanho_da_barra = 0.25
p1 = plt.bar(pos + tamanho_da_barra, sizes_genero[0], tamanho_da_barra, color='pink', edgecolor='black')
plt.bar(pos, sizes_genero[1], tamanho_da_barra, color='blue', edgecolor='black')
plt.xticks(pos, labels_especialidade)
plt.xlabel('Especialidades', fontsize=16)
plt.ylabel('Generos', fontsize=16)
plt.title('Descrição das especialidades de acordo com Genero', fontsize=16)
plt.legend(labels_generos, loc='upper left', ncols=3)

plt.show()
