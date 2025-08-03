import pandas as pd
import os
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(path):
    if not os.path.exists(path):
        print("❌ Cleaned data not found.")
        return None
    df = pd.read_csv(path)
    print("✅ Cleaned data loaded. Shape:", df.shape)
    return df


def detect_anomalies(df):
    numeric_cols = [
        'amount', 'oldBalInitiator', 'newBalInitiator',
        'oldBalRecipient', 'newBalRecipient'
    ]

    df = df.replace([float('inf'), -float('inf')], None)
    df = df.dropna(subset=numeric_cols)

    model = IsolationForest(
        n_estimators=100, contamination=0.01, random_state=42
    )
    df['anomaly'] = model.fit_predict(df[numeric_cols])
    df['anomaly'] = df['anomaly'].map({-1: 1, 1: 0})
    print("✅ Anomaly detection complete.")
    return df


def save_output(df, path):
    df.to_csv(path, index=False)
    print(f"📁 Anomaly-tagged data saved to: {path}")


def plot_anomaly_distribution(df, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    plt.figure(figsize=(6, 4))
    sns.countplot(x='anomaly', data=df)
    plt.title("Anomaly vs Normal Transactions")
    plt.xlabel("Anomaly")
    plt.ylabel("Count")
    plt.xticks([0, 1], ["Normal", "Suspicious"])
    plt.tight_layout()
    plt.savefig(f"{output_folder}/anomaly_distribution.png")
    plt.close()
    print("📊 Anomaly distribution plot saved.")


def plot_anomalies_scatter(df, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    plt.figure(figsize=(10, 5))
    sns.scatterplot(
        data=df,
        x='step',
        y='amount',
        hue='anomaly',
        palette={0: 'blue', 1: 'red'},
        alpha=0.6
    )
    plt.title("Anomaly Detection: Red = Anomaly, Blue = Normal")
    plt.xlabel("Step (Time)")
    plt.ylabel("Transaction Amount")
    plt.legend(title="Anomaly", labels=["Normal", "Suspicious"])
    plt.tight_layout()
    plt.savefig(f"{output_folder}/anomaly_plot.png")
    plt.close()
    print("📈 Scatter plot saved: anomaly_plot.png")


if __name__ == "__main__":
    input_path = "outputs/cleaned_data.csv"
    output_path = "outputs/anomaly_data.csv"

    df = load_data(input_path)
    if df is not None:
        df = detect_anomalies(df)
        save_output(df, output_path)
        plot_anomaly_distribution(df, "outputs")
        plot_anomalies_scatter(df, "outputs")
        