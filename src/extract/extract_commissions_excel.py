import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load source path
source_excel_path = os.getenv("SOURCE_EXCEL_PATH")
excel_file_path = Path(source_excel_path)

print(f"Source file found: {excel_file_path.exists()}")

source_excel = pd.ExcelFile(excel_file_path)

print(f"Sheets found: {source_excel.sheet_names}")

column_mapping = {
    "MESE": "mese_raw",
    "Mese": "mese_raw",
    "OK": "completo_raw",
    "Completo": "completo_raw",
    "SLOT": "slot_raw",
    "Slot": "slot_raw",
    "Priorità": "priorita_raw",
    "Cliente": "cliente_raw",
    "Ordine": "ordine_raw",
    "Stato": "stato_raw",
    "Data ordine": "data_ordine_raw",
    "Deadline": "deadline_raw",
    "Prezzo": "prezzo_raw",
    "Tassa PayPaypal": "tassa_paypal_raw",
    "Entrata": "entrata_raw",
    "Piattaforma di vendita": "contatto_raw",
    "Contatto": "contatto_raw",
    "Online Handle": "online_handle_raw",
    "Note": "note_raw",
}
def extract_commissions_excel(file_path):
    source_excel = pd.ExcelFile(file_path)

    dataframes = []

    for sheet_name in source_excel.sheet_names:
        df_page = source_excel.parse(sheet_name)
        df_page = df_page.rename(columns = column_mapping)
        df_page = df_page.drop(columns=["Colonna 1"], errors="ignore")
        df_page["source_sheet"] = sheet_name
        df_page["source_row"] = df_page.index + 2
        dataframes.append(df_page)
    return pd.concat(dataframes, ignore_index=True)

if __name__ == "__main__":

    df = extract_commissions_excel(excel_file_path)

    print(df.shape)
    print(df.head())
