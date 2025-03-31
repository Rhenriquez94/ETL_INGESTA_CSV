import pandas as pd
import re

CLEANR = re.compile("<.*?>")

def cleanhtml(raw_html):
    if isinstance(raw_html, str):
        return re.sub(CLEANR, "", raw_html)
    return raw_html

def load_data():
    # Leer Questions
    questions = pd.read_csv(
        "data/Questions.csv",
        quotechar='"',
        escapechar='\\',
        encoding='latin1',
        delimiter=',',
        on_bad_lines='skip',
        engine='python'
    )

    # Leer Answers
    answers = pd.read_csv(
        "data/Answers.csv",
        quotechar='"',
        escapechar='\\',
        encoding='latin1',
        delimiter=',',
        on_bad_lines='skip',
        engine='python'
    )

    # Leer Tags
    tags = pd.read_csv("data/Tags.csv")

    # Limpiar HTML de columnas Body
    if 'Body' in questions.columns:
        questions['Body'] = questions['Body'].apply(cleanhtml)

    if 'Body' in answers.columns:
        answers['Body'] = answers['Body'].apply(cleanhtml)

    return questions, answers, tags

if __name__ == "__main__":
    questions, answers, tags = load_data()

print(questions())