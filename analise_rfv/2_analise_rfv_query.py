from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt

# Variáveis de ambiente
load_dotenv()
host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')
port = os.getenv('port')

db_user = user     
db_password = password
db_host = host  
db_port = port       
db_name = database     

# String de conexão para MySQL usando PyMySQL
db_string = f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

# Criando a engine do SQLAlchemy
engine = create_engine(db_string)

query = '''
WITH CATEGORIZADO AS (
SELECT CUSTOMERID, RECENCIA, FREQUENCIA, VALOR_MONET,
CASE
WHEN RECENCIA =  5 AND FREQUENCIA = 5 AND VALOR_MONET = 5 THEN 'Campeões'
WHEN RECENCIA >= 3 AND FREQUENCIA >= 4 AND VALOR_MONET >= 3 THEN 'Clientes Fiéis'
WHEN RECENCIA >= 3 AND FREQUENCIA = 3  AND VALOR_MONET >= 3 THEN 'Potencial para Fiéis'
WHEN RECENCIA >= 4 AND FREQUENCIA <= 2 THEN 'Novos Clientes'
WHEN RECENCIA >= 4 AND FREQUENCIA > 2 AND VALOR_MONET IN (1,2) THEN 'Promissores' 
WHEN RECENCIA BETWEEN 1 AND 3 AND FREQUENCIA BETWEEN 1 AND 5 AND VALOR_MONET IN (3,4) THEN 'Clientes que Precisam de Atenção'
WHEN RECENCIA BETWEEN 1 AND 3 AND FREQUENCIA BETWEEN 1 AND 5 AND VALOR_MONET = 5 THEN 'Não Pode Perder'
WHEN RECENCIA BETWEEN 1 AND 3 AND FREQUENCIA IN (3,4) AND VALOR_MONET IN (1,2) THEN 'Quase Dormindo'
WHEN RECENCIA BETWEEN 1 AND 3 AND FREQUENCIA IN (1,2) AND VALOR_MONET = 2 THEN 'Em Risco'
WHEN RECENCIA BETWEEN 1 AND 3 AND FREQUENCIA IN (1,2) AND VALOR_MONET = 1 THEN 'Perdidos ou Hibernando'
ELSE 'Sem Categoria'
END AS CATEGORIA 
FROM RFV_TABELA
)
SELECT CATEGORIA, COUNT(*) AS NUM_CLIENTES,
ROUND((COUNT(*) * 100.0 / SUM(COUNT(*)) OVER()), 2) AS PORCENTAGEM
FROM CATEGORIZADO
GROUP BY CATEGORIA
ORDER BY NUM_CLIENTES DESC
'''
print(pd.read_sql_query(query, con=engine))

resultados_categorias = pd.read_sql_query(query, con=engine)

fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.bar(resultados_categorias['CATEGORIA'], resultados_categorias['PORCENTAGEM'], 
              color='#7B68EE')
ax.set_xlabel('Categoria')
ax.set_ylabel('Percentual (%)')
ax.set_title('Distribuição de Clientes por Categoria')
ax.set_xticklabels(resultados_categorias['CATEGORIA'], rotation=45, ha='right')
ax.bar_label(bars, fmt='%.2f')
plt.tight_layout()
plt.show()