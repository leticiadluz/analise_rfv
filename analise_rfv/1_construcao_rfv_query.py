from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd
import os
from dotenv import load_dotenv

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

#Análise Recência, Frequência e Valor
query = '''

CREATE TABLE RFV_TABELA AS
WITH 
DATA_MAXIMA AS ( 
SELECT MAX(INVOICEDATE) AS DATA_MAX
FROM online_retail_table
WHERE INVOICENO NOT LIKE 'C%%'
AND STOCKCODE REGEXP '[0-9]{5,}'
),

ULTIMA_COMPRA AS (
SELECT CUSTOMERID, MAX(INVOICEDATE) AS DATA_ULTIMA_COMPRA
FROM online_retail_table
WHERE INVOICENO NOT LIKE 'C%%'
AND STOCKCODE REGEXP '[0-9]{5,}'
GROUP BY CUSTOMERID
),

COMPRAS_CLIENTES AS (
SELECT CUSTOMERID, COUNT(CUSTOMERID) AS QTD_COMPRAS
FROM online_retail_table
WHERE INVOICENO NOT LIKE 'C%%'
AND STOCKCODE REGEXP '[0-9]{5,}'
GROUP BY CUSTOMERID
),

VALOR_TOTAL AS (
SELECT CUSTOMERID, SUM(QUANTITY * UNITPRICE) AS TOTAL_CLIENTE
FROM online_retail_table
WHERE INVOICENO NOT LIKE 'C%%'
AND STOCKCODE REGEXP '[0-9]{5,}'
GROUP BY CUSTOMERID
)

SELECT o.CUSTOMERID, o.INVOICEDATE, c.QTD_COMPRAS, vt.TOTAL_CLIENTE,
DATEDIFF(dm.DATA_MAX, uc.DATA_ULTIMA_COMPRA) / 7 AS DIF_SEMANAS,
NTILE(5) OVER (ORDER BY DATEDIFF(dm.DATA_MAX, uc.DATA_ULTIMA_COMPRA) / 7 DESC) AS RECENCIA,
NTILE(5) OVER (ORDER BY c.QTD_COMPRAS) AS FREQUENCIA,
NTILE(5) OVER (ORDER BY vt.TOTAL_CLIENTE) AS VALOR_MONET
FROM online_retail_table o

JOIN COMPRAS_CLIENTES c ON o.CUSTOMERID = c.CUSTOMERID  
JOIN VALOR_TOTAL vt ON o.CUSTOMERID = vt.CUSTOMERID  
JOIN ULTIMA_COMPRA uc ON o.CUSTOMERID = uc.CUSTOMERID
CROSS JOIN DATA_MAXIMA dm

WHERE o.INVOICENO NOT LIKE 'C%%'
AND o.STOCKCODE REGEXP '[0-9]{5,}'
'''

with engine.connect() as connection:
    connection.execute(text(query))