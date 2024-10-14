import pandas as pd
import mysql.connector
import importlib.metadata

# Obter as versões
pandas_version = pd.__version__
mysql_connector_version = mysql.connector.__version__

# Usar importlib.metadata para obter a versão do dotenv
dotenv_version = importlib.metadata.version('python-dotenv')

print("Versão do pandas:", pandas_version)
print("Versão do mysql-connector:", mysql_connector_version)
print("Versão do python-dotenv:", dotenv_version)
