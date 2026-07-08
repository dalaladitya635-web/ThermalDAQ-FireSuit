"""
Synthetic Thermal Sensor Dataset Generator

This module generates realistic thermal sensor data inspired by
fire suit testing experiments.

Author: Aditya Dalal
"""

import os
import numpy as np
import pandas as pd


NUM_SENSORS = 134
NUM_TIME_STEPS = 500

np.random.seed(42)


def generate_temperature_curve():

    """
    Simulates a realistic fire exposure.

    Ambient
        ↓
    Heating
        ↓
    Peak Fire
        ↓
    Cooling
    """

    ambient = 28

    heating = np.linspace(
        ambient,
        np.random.uniform(650, 850),
        250
    )

    cooling = np.linspace(
        heating[-1],
        np.random.uniform(80, 120),
        250
    )

    curve = np.concatenate([heating, cooling])

    noise = np.random.normal(
        0,
        4,
        NUM_TIME_STEPS
    )

    return curve + noise


def generate_dataset():

    data = {}

    data["Time"] = np.arange(NUM_TIME_STEPS)

    for i in range(1, NUM_SENSORS + 1):

        data[f"Sensor_{i}"] = generate_temperature_curve()

    df = pd.DataFrame(data)

    os.makedirs("data", exist_ok=True)

    df.to_csv(
        "data/fire_suit_sensor_data.csv",
        index=False
    )

    print("\nDataset Generated Successfully!")

    print(df.head())

    print("\nShape")

    print(df.shape)


if __name__ == "__main__":

    generate_dataset()