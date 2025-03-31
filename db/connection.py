import pandas as pd
from sqlalchemy import create_engine

# Parámetros de conexión
DB_USER = "pwd"
DB_PASSWORD = "pwd"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "ingesta_csv"

# Crear conexión
def get_engine():
    return create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

