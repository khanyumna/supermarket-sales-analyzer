import pandas as pd
import sqlite3

def load_and_prepare_data(file_path, db_file):
    # Load dataset
    try:
        df = pd.read_csv(file_path)
        print("Dataset successfully loaded!")
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}.")
        exit()

    # Add missing columns
    if 'Date' not in df.columns:
        df['Date'] = pd.date_range(start="2023-01-01", periods=len(df), freq="D")
    if 'Revenue' not in df.columns:
        df['Revenue'] = df['Unit price'] * df['Quantity']
    if 'Costs' not in df.columns:
        df['Costs'] = df['Tax 5%']
    if 'Profit_Margins' not in df.columns:
        df['Profit_Margins'] = (df['Revenue'] - df['Costs']) / df['Revenue']

    # Convert Date column to datetime and create 'Days' column
    df['Date'] = pd.to_datetime(df['Date'])
    df['Days'] = (df['Date'] - df['Date'].min()).dt.days

    # rolling averages
    df['Costs_Rolling_Avg'] = df['Costs'].rolling(window=3, min_periods=1).mean()
    df['Revenue_Rolling_Avg'] = df['Revenue'].rolling(window=3, min_periods=1).mean()
    df['Units_Sold_Rolling_Avg'] = df['Quantity'].rolling(window=3, min_periods=1).mean()

    # Drop rows with missing values
    df = df.dropna().reset_index(drop=True)

    # Save to SQLite database
    connection = sqlite3.connect(db_file)
    df.to_sql("sales", connection, if_exists="replace", index=False)
    connection.close()

    print("\nDataset prepared and saved to database!")
    return df
