# Biblioteca
import pandas as pd

# Lendo as planilhas
planilhas = pd.read_excel('online_retail_II.xlsx', sheet_name=None)

# Acessando cada planilha individualmente
planilha1 = planilhas['Year 2009-2010']
planilha2 = planilhas['Year 2010-2011']

# Combinando as duas planilhas em um único DataFrame
planilha_combinada = pd.concat([planilha1, planilha2])

print(planilha_combinada.head())
print(planilha_combinada.shape)
print(planilha_combinada.isnull().sum())

# Removendo linhas com valores nulos
planilha_combinada.dropna(inplace=True)
print(planilha_combinada.isnull().sum())

# Salvando o DataFrame combinado em um arquivo CSV
planilha_combinada.to_csv('online_retail.csv', index=False)

