import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option(
    "display.max_rows", 1000, "display.min_rows", 200,
    "display.max_columns", None, "display.width", None)

df = pd.read_csv('BD/atendimentos_2021_outros.csv')

df_new = df.loc[:, ['Especialidade', 'Data']]


df_new['Data'] = pd.to_datetime(df['Data'], dayfirst=True)
df_new = df_new.groupby(['Especialidade', pd.Grouper(key='Data', freq='D')]).sum()
df_new.sort_values(by='Data')

for name, data in df_new.index:
    print(name)
    print(data)
