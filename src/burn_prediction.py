import pandas as pd


def classify_burn(temp):
    """
    Classify burn severity based on temperature.
    (Simplified model for educational purposes)
    """
    if temp < 44:
        return "Safe"

    elif temp < 60:
        return "First Degree"

    elif temp < 72:
        return "Second Degree"

    else:
        return "Third Degree"


def predict_burns(df):

    sensors = df.columns[1:]

    latest = df.iloc[-1]

    results = {}

    for sensor in sensors:

        temperature = latest[sensor]

        results[sensor] = {
            "Temperature": temperature,
            "Prediction": classify_burn(temperature)
        }

    return results


def main():

    df = pd.read_csv("data/sample_sensor_data.csv")

    predictions = predict_burns(df)

    print("\n========== BURN PREDICTION ==========\n")

    for sensor, info in predictions.items():

        print(
            f"{sensor:<10} | "
            f"{info['Temperature']:>5} °C | "
            f"{info['Prediction']}"
        )


if __name__ == "__main__":
    main()