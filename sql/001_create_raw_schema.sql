CREATE SCHEMA IF NOT EXISTS raw;

CREATE TABLE IF NOT EXISTS raw.commissions_excel (
    id BIGSERIAL PRIMARY KEY,
    source_sheet TEXT NOT NULL,
    source_row INTEGER NOT NULL,
    mese_raw TEXT,
    slot_raw TEXT,
    completo_raw TEXT,
    priorita_raw TEXT,
    cliente_raw TEXT,
    ordine_raw TEXT,
    stato_raw TEXT,
    data_ordine_raw TEXT,
    deadline_raw TEXT,
    prezzo_raw TEXT,
    tassa_paypal_raw TEXT,
    entrata_raw TEXT,
    contatto_raw TEXT,
    online_handle_raw TEXT,
    note_raw TEXT,
    loaded_at TIMESTAMPTZ DEFAULT NOW()
);