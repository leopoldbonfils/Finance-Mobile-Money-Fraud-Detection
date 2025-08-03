import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


def load_data(path):
    if not os.path.exists(path):
        print(f"❌ File not found: {path}")
        return None
    df = pd.read_csv(path)
    print("✅ Cleaned data loaded. Shape:", df.shape)
    return df


def show_summary(df):
    print("\n🔢 Summary statistics:")
    print(df.describe())

    if 'isFraud' in df.columns:
        print("\n📊 Fraud label counts:")
        print(df['isFraud'].value_counts())


def create_plots(df, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    # Plot 1
    plt.figure(figsize=(8, 4))
    sns.histplot(df['amount'], bins=50, kde=True)
    plt.title("Transaction Amount Distribution")
    plt.xlabel("Amount")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(f"{output_folder}/amount_distribution.png")
    plt.close()

    # Plot 2
    if 'isFraud' in df.columns:
        plt.figure(figsize=(6, 4))
        sns.countplot(x='isFraud', data=df)
        plt.title("Fraud vs Non-Fraud Transactions")
        plt.xlabel("Is Fraud")
        plt.ylabel("Count")
        plt.xticks([0, 1], ["Legit", "Fraud"])
        plt.tight_layout()
        plt.savefig(f"{output_folder}/fraud_count.png")
        plt.close()

    # Plot 3
    plt.figure(figsize=(10, 4))
    sns.lineplot(data=df, x='step', y='amount')
    plt.title("Transaction Amount Over Time (Step)")
    plt.xlabel("Step")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.savefig(f"{output_folder}/step_vs_amount.png")
    plt.close()

    # Plot 4
    if 'isFraud' in df.columns:
        plt.figure(figsize=(8, 5))
        sns.boxplot(x='isFraud', y='amount', data=df)
        plt.title("Transaction Amount by Fraud Status")
        plt.xlabel("Is Fraud")
        plt.ylabel("Amount")
        plt.xticks([0, 1], ["Legit", "Fraud"])
        plt.tight_layout()
        plt.savefig(f"{output_folder}/boxplot_amount_fraud.png")
        plt.close()

    # Plot 5
    plt.figure(figsize=(10, 6))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", square=True)
    plt.title("Correlation Heatmap of Numeric Features")
    plt.tight_layout()
    plt.savefig(f"{output_folder}/correlation_heatmap.png")
    plt.close()


# ✅ Add this to actually run the script
if __name__ == "__main__":
    df = load_data("outputs/cleaned_data.csv")
    if df is not None:
        show_summary(df)
        create_plots(df, "outputs")
        print("📊 EDA complete. Charts saved in outputs/")
