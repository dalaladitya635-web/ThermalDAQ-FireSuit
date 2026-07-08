import pandas as pd


SENSITIVITY = 0.005      # Example sensor sensitivity (V/(kW/m²))


def calculate_heat_flux(sensor_voltage):
    """
    Calculate heat flux using:
    q = U / S
    """
    return sensor_voltage / SENSITIVITY


def main():

    df = pd.read_csv("data/sample_sensor_data.csv")

    print("\nHEAT FLUX CALCULATIONS\n")

    for sensor in df.columns[1:]:

        voltage = df[sensor] / 1000

        heat_flux = calculate_heat_flux(voltage)

        print(f"\n{sensor}")

        print(heat_flux.head())


if __name__ == "__main__":
    main()