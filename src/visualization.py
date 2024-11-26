import matplotlib.pyplot as plt

def plot_feature_importance(model, feature_names):
    """
    Plots the feature importance.
    """
    importance = model.feature_importances_
    plt.figure(figsize=(8, 5))
    plt.barh(feature_names, importance)
    plt.xlabel('Feature Importance')
    plt.ylabel('Feature')
    plt.title('Feature Importance for Stock Prediction Model')
    plt.show()
