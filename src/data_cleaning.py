import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    df['Start_Date'] = pd.to_datetime(df['Start_Date'], errors='coerce')
    df['End_Date'] = pd.to_datetime(df['End_Date'], errors='coerce')
    df = df.dropna(subset=['Revenue', 'Cost', 'Start_Date', 'End_Date'])
    df['Profit'] = df['Revenue'] - df['Cost']
    df['ROI'] = (df['Profit'] / df['Cost']) * 100
    df['Project_Duration'] = (df['End_Date'] - df['Start_Date']).dt.days
    df['Month'] = df['Start_Date'].dt.strftime('%b-%Y')
    df['Status'] = df['Profit'].apply(lambda x: 'Profit' if x >= 0 else 'Loss')
    return df
