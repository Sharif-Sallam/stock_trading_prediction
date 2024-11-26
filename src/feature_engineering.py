def preprocess_data(data):
    """
    Adds features and target variable for stock prediction.
    """
    # Feature engineering
    data['Daily_Return'] = data['Close'].pct_change()
    data['5Day_MA'] = data['Close'].rolling(window=5).mean()
    data['10Day_MA'] = data['Close'].rolling(window=10).mean()
    data['Volatility'] = data['High'] - data['Low']
    
    # Target variable: 1 if next day's price is higher, else 0
    data['Target'] = (data['Close'].shift(-1) > data['Close']).astype(int)
    
    # Drop rows with NaN values
    data = data.dropna()
    return data
