SELECT
    source_sheet,
    source_row,
    mese_raw,
    slot_raw,
    completo_raw,
    priorita_raw,
    cliente_raw,
    ordine_raw,
    stato_raw,
    data_ordine_raw,
    deadline_raw,
    prezzo_raw,
    tassa_paypal_raw,
    entrata_raw,
    contatto_raw,
    online_handle_raw,
    loaded_at,
    note_raw

FROM {{ source('commissions_raw', 'commissions_excel') }}

-- Exclude known source anomaly
WHERE NOT (
    source_sheet = '2026'
    AND UPPER(BTRIM(COALESCE(mese_raw, ''))) = 'V-GEN'
)