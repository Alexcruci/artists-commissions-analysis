import os

import psycopg
from dotenv import load_dotenv

from pathlib import Path
from src.extract.extract_commissions_excel import extract_commissions_excel

import pandas as pd
# Load environment variables
load_dotenv()

source_path = Path(os.getenv("SOURCE_EXCEL_PATH"))

df = extract_commissions_excel(source_path)

print(f"Extracted rows: {len(df)}")
print(f"DataFrame shape: {df.shape}")

def to_raw_text(value):
    if pd.isna(value):
            return None
    else:
        return str(value)
    
columns = [
    "source_sheet",
    "source_row",
    "mese_raw",
    "slot_raw",
    "completo_raw",
    "priorita_raw",
    "cliente_raw",
    "ordine_raw",
    "stato_raw",
    "data_ordine_raw",
    "deadline_raw",
    "prezzo_raw",
    "tassa_paypal_raw",
    "entrata_raw",
    "contatto_raw",
    "online_handle_raw",
    "note_raw",
]

rows = []

for _, row in df.iterrows():

    values = [
        str(row["source_sheet"]),
        int(row["source_row"]),
    ]

    for column in columns[2:]:
        values.append(to_raw_text(row[column]))

    rows.append(tuple(values))

if not rows:
        raise ValueError("No rows extracted. Aborting database refresh.")

print("Rows prepared:", len(rows))
print("Fields per row:", len(rows[0]))
print("source_row type:", type(rows[0][1]))

assert all(len(row) == len(columns) for row in rows)

column_names = ", ".join(columns)

placeholders = ", ".join(["%s"] * len(columns))

insert_query = f"""
    INSERT INTO raw.commissions_excel ({column_names})
    VALUES ({placeholders})
"""
# Connect to PostgreSQL
with psycopg.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
) as connection:

  # Connect to PostgreSQL

    with psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    ) as connection:

        with connection.cursor() as cursor:

            cursor.execute(
                "TRUNCATE TABLE raw.commissions_excel RESTART IDENTITY;"
            )

            cursor.executemany(insert_query, rows)

            cursor.execute(
                "SELECT COUNT(*) FROM raw.commissions_excel;"
            )

            count = cursor.fetchone()[0]

    print(f"Rows in database: {count}")
