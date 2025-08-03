import pandas as pd
import os


def main():
    input_path = "data/synthetic_mobile_money_transaction_dataset.csv"
    output_path = "outputs/cleaned_data.csv"

    if not os.path.exists(input_path):
        print("❌ File not found:", input_path)
        return

    df = pd.read_csv(input_path)
    print("📦 Original dataset shape:", df.shape)

    # Drop rows with missing values
    df = df.dropna()

    # Convert 'timestamp' column to datetime format if it exists
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

    # Save the cleaned dataset
    df.to_csv(output_path, index=False)
    print("✅ Cleaned data saved to:", output_path)


if __name__ == "__main__":
    main()
