import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

df = pd.read_csv("atendimentos_2021_outros.csv")

pd.set_option('display.max_columns', df.columns.size)
pd.set_option('display.expand_frame_repr', False)

df['Sexo'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribuição de gênero dos pacientes')
plt.axis('equal')
plt.show()
