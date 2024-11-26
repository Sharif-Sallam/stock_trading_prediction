from src.data_loader import load_data
from src.feature_engineering import preprocess_data
from src.model_training import train_model, evaluate_model
from src.visualization import plot_feature_importance

# Define the main workflow
def main():
    # Step 1: Load the dataset
    print("Loading data...")
    file_path = "data/stock_data.csv"  # Path to the test data
    data = load_data(file_path)

    # Step 2: Preprocess the data
    print("Preprocessing data...")
    data = preprocess_data(data)

    # Step 3: Split the data into training and testing sets
    print("Splitting data...")
    from sklearn.model_selection import train_test_split
    X = data[['Daily_Return', '5Day_MA', '10Day_MA', 'Volatility', 'Volume']]
    y = data['Target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Step 4: Train the model
    print("Training model...")
    model = train_model(X_train, y_train)

    # Step 5: Evaluate the model
    print("Evaluating model...")
    evaluate_model(model, X_test, y_test)

    # Step 6: Visualize feature importance
    print("Visualizing feature importance...")
    plot_feature_importance(model, X_train.columns)

if __name__ == "__main__":
    main()
