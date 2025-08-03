import pandas as pd
import os
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt


def load_data(path):
    if not os.path.exists(path):
        print("❌ Anomaly-tagged data not found.")
        return None
    df = pd.read_csv(path)
    print("✅ Data loaded. Shape:", df.shape)
    return df


def evaluate_model(df):
    if 'isFraud' not in df.columns or 'anomaly' not in df.columns:
        print("❌ Columns 'isFraud' or 'anomaly' missing.")
        return

    y_true = df['isFraud']
    y_pred = df['anomaly']

    print("📊 Confusion Matrix:")
    cm = confusion_matrix(y_true, y_pred)
    print(cm)

    print("\n📋 Classification Report:")
    print(classification_report(
        y_true, y_pred, target_names=["Legit", "Fraud"]
    ))

    # Plot confusion matrix
    plt.figure(figsize=(5, 4))
    sns.heatmap(
        cm, annot=True, fmt="d", cmap="Blues",
        xticklabels=["Normal", "Anomaly"],
        yticklabels=["Legit", "Fraud"]
    )
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.tight_layout()
    plt.savefig("outputs/confusion_matrix.png")
    plt.close()
    print("✅ Confusion matrix saved to outputs/confusion_matrix.png")


if __name__ == "__main__":
    df = load_data("outputs/anomaly_data.csv")
    if df is not None:
        evaluate_model(df)
