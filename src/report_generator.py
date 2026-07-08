import os
import pandas as pd

from burn_prediction import predict_burns


def generate_report():
    df = pd.read_csv("data/sample_sensor_data.csv")

    predictions = predict_burns(df)

    os.makedirs("reports", exist_ok=True)

    with open("reports/fire_suit_report.txt", "w") as file:

        file.write("THERMALDAQ FIRE SUIT ANALYSIS REPORT\n")
        file.write("=" * 50 + "\n\n")

        for sensor, info in predictions.items():
            file.write(
                f"{sensor}\n"
                f"Temperature : {info['Temperature']} °C\n"
                f"Prediction  : {info['Prediction']}\n\n"
            )

    print("Report Generated Successfully!")


if __name__ == "__main__":
    generate_report()