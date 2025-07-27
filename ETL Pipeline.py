import pandas as pd
from sqlalchemy import create_engine

# Database connection details
DB_USER = "postgres"
DB_PASSWORD = "Devi$1513"
DB_HOST = "localhost"  # Change if needed
DB_PORT = "5432"
DB_NAME = "ETL-DB"

# Excel file path
EXCEL_FILE = r"C:\Users\gchau\OneDrive\Documents\names.xlsx"
# Step 1: Extract - Read data from Excel
df = pd.read_excel(EXCEL_FILE)

# Step 2: Transform - Basic cleaning (Optional)
df['Full Name'] = df['First Name'] + df["Last Name"]
print(df)

# Step 3: Load - Insert into PostgreSQL
try:
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    df.to_sql("names1", engine, if_exists="replace", index=False)
    print("Data loaded successfully!")
except Exception as e:
    print("Error loading data:", e)
