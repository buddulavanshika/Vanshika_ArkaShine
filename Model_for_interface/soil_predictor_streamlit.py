import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors

# Load the model and scaler
model = joblib.load("best_knn_model.pkl")
scaler = joblib.load("scaler.pkl")
target_columns = joblib.load("target_columns.pkl")  # List of target nutrient names
feature_columns = joblib.load("feature_names.pkl")  # List of 18 features


st.title("🌾 Soil Nutrient Predictor")

st.markdown("Enter the reflectance values for the following 18 wavelengths:")

# Dynamically generate number inputs for all 18 features
input_data = {}
for feature in feature_columns:
    input_data[feature] = st.number_input(f"{feature}", min_value=0.0, value=100.0)

# When the user clicks 'Predict'
if st.button("Predict Nutrient Levels"):
    df_input = pd.DataFrame([input_data])  # Convert to DataFrame
    scaled_input = scaler.transform(df_input)
    prediction = model.predict(scaled_input)

    # Format predictions
    predicted_values = {target_columns[i]: prediction[0][i] for i in range(len(target_columns))}

    st.subheader("🧪 Predicted Nutrient Levels:")
    st.write(predicted_values)

    # Bar chart to display predicted values
    colors = list(mcolors.TABLEAU_COLORS.values())
    fig, ax = plt.subplots()
    bars = ax.barh(list(predicted_values.keys()), list(predicted_values.values()), color=colors[:len(predicted_values)])
    ax.set_xlabel('Predicted Levels')
    ax.set_title('Predicted Nutrient Levels')
    for bar, value in zip(bars, predicted_values.values()):
        ax.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{value:.2f}', va='center')
    st.pyplot(fig)
