import pandas as pd


def load_sensor_data(file_path):
    """
    Load sensor data from a CSV file.
    """
    df = pd.read_csv(file_path)
    return df


def display_summary(df):
    """
    Display basic information about the dataset.
    """
    print("\n========== DATASET SUMMARY ==========\n")

    print(df.head())

    print("\nShape:", df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nStatistics:")
    print(df.describe())


if __name__ == "__main__":
    data = load_sensor_data("data/sample_sensor_data.csv")
    display_summary(data)