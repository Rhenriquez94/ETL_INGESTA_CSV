import pandas as pd
import logging
from db.connection import get_engine

# Configuración del logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Carga por chunks a la base de datos
def load_data(df: pd.DataFrame, table_name: str, chunksize: int = 300000):
    engine = get_engine()

    if table_name.endswith('_cleaned'):
        table_name = table_name.replace('_cleaned', '')

    try:
        for i, chunk in enumerate(range(0, len(df), chunksize)):
            df.iloc[chunk:chunk + chunksize].to_sql(
                table_name,
                engine,
                if_exists="append" if chunk > 0 else "replace",
                index=False
            )
            logging.info(f"Chunk {i + 1} cargado correctamente en '{table_name}'.")
        logging.info(f"Datos cargados completamente en la tabla '{table_name}'.")
    except Exception as e:
        logging.error(f"Error al cargar datos: {e}")
