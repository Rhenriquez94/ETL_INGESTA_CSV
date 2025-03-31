import pandas as pd
import logging

# Configurar logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def transform_data(questions: pd.DataFrame, answers: pd.DataFrame, tags: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    # Convertir fechas a datetime
    questions['CreationDate'] = pd.to_datetime(questions['CreationDate'], errors='coerce')
    answers['CreationDate'] = pd.to_datetime(answers['CreationDate'], errors='coerce')

    logging.info("✅ Transformación de fechas realizada correctamente.")

    return questions, answers, tags
