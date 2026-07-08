import os
import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    """
    Load sensor data from CSV.
    """
    return pd.read_csv(file_path)


def plot_temperature(df):
    """
    Plot temperature of all sensors against time.
    """

    plt.figure(figsize=(12, 7))

    time = df["Time"]

    for column in df.columns[1:]:
        plt.plot(time, df[column], linewidth=2, label=column)

    plt.title("Temperature vs Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.legend(loc="upper left", fontsize=8)

    os.makedirs("images", exist_ok=True)

    plt.savefig("images/temperature_plot.png", dpi=300)

    plt.show()


if __name__ == "__main__":

    df = load_data("data/sample_sensor_data.csv")

    plot_temperature(df)