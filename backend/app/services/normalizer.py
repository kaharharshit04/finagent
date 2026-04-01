STANDARD_COLUMNS = ["date", "amount", "description"]

def normalize(df):
    df.columns = [col.lower() for col in df.columns]

    mapping = {
        "amt": "amount",
        "value": "amount",
        "transaction_date": "date",
        "details": "description",
        "desc": "description"
    }

    df = df.rename(columns=mapping)

    # Ensure required columns exist
    for col in STANDARD_COLUMNS:
        if col not in df.columns:
            df[col] = None

    return df[STANDARD_COLUMNS]