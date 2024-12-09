import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

print("Caminho do .env:", os.path.abspath('.'))
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

if not all([POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, DATABASE_PORT, POSTGRES_DB]):
    print("Erro: Variáveis de ambiente não carregadas corretamente!")
else:
    print("Variáveis carregadas corretamente!")