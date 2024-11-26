import pandas as pd

def load_data(file_path):
    """
    Loads stock data from a CSV file.
    """
    try:
        data = pd.read_csv(file_path)
        data['Date'] = pd.to_datetime(data['Date'])
        data.set_index('Date', inplace=True)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
