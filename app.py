import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from src.heat_flux import calculate_heat_flux
from src.burn_prediction import classify_burn

st.set_page_config(
    page_title="ThermalDAQ FireSuit",
    page_icon="🔥",
    layout="wide"
)

st.title("🔥 ThermalDAQ FireSuit")
st.markdown("### Thermal Protective Clothing Analysis Dashboard")

uploaded_file = st.file_uploader(
    "Upload Thermal Sensor CSV",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("Dataset Loaded Successfully!")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Temperature Plot")

    fig, ax = plt.subplots(figsize=(14,6))

    for sensor in df.columns[1:]:
        ax.plot(df["Time"], df[sensor], alpha=0.6)

    ax.set_xlabel("Time")
    ax.set_ylabel("Temperature (°C)")
    ax.grid(True)

    st.pyplot(fig)

    st.subheader("Dataset Statistics")

    st.dataframe(df.describe())

    latest = df.iloc[-1]

    results = []

    for sensor in df.columns[1:]:

        temp = latest[sensor]

        voltage = temp / 1000

        heat_flux = calculate_heat_flux(voltage)

        burn = classify_burn(temp)

        results.append({
            "Sensor": sensor,
            "Temperature (°C)": round(temp,2),
            "Heat Flux": round(heat_flux,2),
            "Burn Prediction": burn
        })

    st.subheader("Burn Prediction Results")

    st.dataframe(pd.DataFrame(results))