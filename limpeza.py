# Biblioteca
import pandas as pd

planilhas = pd.read_excel('online_retail_II.xlsx', sheet_name=None)
planilha1 = planilhas['Year 2009-2010']
planilha2 = planilhas['Year 2010-2011']

planilha_combinada = pd.concat([planilha1, planilha2])

print(planilha_combinada.head())
print(planilha_combinada.shape)
print(planilha_combinada.isnull().sum())

planilha_combinada.dropna(inplace=True)
print(planilha_combinada.isnull().sum())
planilha_combinada.to_csv('online_retail.csv', index=False)

