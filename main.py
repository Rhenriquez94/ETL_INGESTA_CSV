import logging
from scripts.extract import load_data
from scripts.transform import transform_data
from scripts.load import load_data as load_to_db

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

if __name__ == "__main__":
    logging.info("🚀 Iniciando proceso ETL...")

    # ETAPA 1: Extracción
    questions, answers, tags = load_data()

    # ETAPA 2: Transformación
    questions, answers, tags = transform_data(questions, answers, tags)

    # ETAPA 3: Carga a PostgreSQL
    load_to_db(questions, "questions")
    load_to_db(answers, "answers")
    load_to_db(tags, "tags")

    logging.info("✅ Proceso ETL finalizado con éxito.")
