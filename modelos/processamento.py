#Bibliotecas
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

db_string = f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
engine = create_engine(db_string)

query = '''
SELECT * FROM tabela_rfv
ORDER BY RAND()
LIMIT 30000;
'''
df_clusterizacao = pd.read_sql_query(query, con=engine)
print(df_clusterizacao.head())
print(df_clusterizacao.info())
df_clusterizacao.to_pickle('df_clusterizacao.pkl')
