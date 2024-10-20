# Bibliotecas
import pandas as pd
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Variáveis de ambiente
load_dotenv()
host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')
port = os.getenv('port')

online_retail = pd.read_csv('online_retail.csv')
                                           
try:
    conexao = mysql.connector.connect(
        host= host,       
        user= user,            
        password= password,  
        database= database,      
        port= port               
    )

    if conexao.is_connected():
        cursor = conexao.cursor()

        criar_tabela = """
        CREATE TABLE IF NOT EXISTS online_retail_table (
            InvoiceNo VARCHAR(20),
            StockCode VARCHAR(20),
            Description TEXT,
            Quantity INT,
            InvoiceDate DATETIME,
            UnitPrice FLOAT,
            CustomerID INT,
            Country VARCHAR(50)
        );
        """
        cursor.execute(criar_tabela)

        inserir_dados_query = """
        INSERT INTO online_retail_table (InvoiceNo, StockCode, Description, 
        Quantity, InvoiceDate, UnitPrice, CustomerID, Country)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        for _, row in online_retail.iterrows():
            cursor.execute(inserir_dados_query, tuple(row))
      
        conexao.commit()

        print("Dados armazenados com sucesso!")

except Error as e:
    print(f"Erro ao conectar ao MySQL: {e}")

finally:
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print("Conexão com MySQL encerrada.")