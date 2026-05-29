EXPECTED_COLUMNS = [
    "Date received",
    "Product",
    "Issue",
    "Consumer complaint narrative",
    "Company",
    "State",
    "Complaint ID"
]

def validate_schema(df):

    missing_columns = [
        col
        for col in EXPECTED_COLUMNS
        if col not in df.columns
    ]

    return missing_columns
