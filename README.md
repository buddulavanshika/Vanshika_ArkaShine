# 🌱 Soil Nutrient Predictor using Spectroscopy and Machine Learning

This project aims to provide a real-time, non-invasive system for analyzing soil health by predicting key nutrient concentrations using visible and near-infrared (vis-NIR) spectroscopic data. The system leverages machine learning models to interpret spectral reflectance and offers an intuitive user interface through a Streamlit web application.

---

## 📌 Problem Statement

Conventional soil analysis methods are time-consuming, labor-intensive, and expensive. They often delay critical agricultural decisions like fertilization planning and crop selection. This project addresses these limitations by developing a machine learning-based system capable of accurately predicting soil nutrient concentrations based on reflectance at different wavelengths. The project integrates an easy-to-use web interface to ensure accessibility for farmers, researchers, and agronomists.

---

## 📊 Dataset Overview

- **Original Samples:** 100 rows of soil spectral and nutrient data.
- **Interpolation Applied:** Dataset expanded to 1000 samples for better model training.
- **Input Features (18):** Spectral reflectance at wavelengths (e.g., A(410), B(435), ..., T(730)).
- **Target Variables (13):** Soil properties and nutrient levels such as:
  - pH
  - EC (dS/m)
  - Organic Carbon (OC %)
  - P, K, Ca, Mg (macronutrients)
  - S, Fe, Mn, Cu, Zn, B (micronutrients)

---
## Feature Importance

Permutation importance was used to determine which spectral bands (wavelengths) contributed most to each nutrient prediction. This enhances model interpretability and informs band selection for future models.

---
## Technologies Used
- **Python**
- **Scikit-Learn**
- **NumPy, Pandaas**
- **Matplotlib, Seaborn**
- **Streamlit- for the interactive web application**

 ---
 ## Models Implemented
 - **Random Forest Regressor**
 - **Gaussian Process Regressor**
 - **KNeighbors Regressor**
 - **Partial Least Square Regression**
---
 
## Streamlit Web Application
A user-friendly web interface was created using Streamlit, allowing users to:
- **Input new spectral reflectance values**
- **Receive real-time predictions for 13 soil parameters**
- **Visualize model outputs.**
👉 **[Live Demo](https://arkashinevanshika.streamlit.app)**
---
## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip
---
### Installation

1. Clone the repository:

```bash
git clone https://github.com/buddulavanshika/Vanshika_Arkashine.git
cd soil-nutrient-predictor
```
2. Install Dependencies:
```bash
pip install -r requirements.txt
```
3. Run the Streamlit app:
```bash
streamlit run soil_predictor_streamlit.py
```
---
# Conclusion
This project provides a robust, data-driven solution to soil nutrient analysis by integrating spectroscopic sensing with machine learning. The approach is fast, scalable, and cost-efficient — making it suitable for real-time field deployment. The Streamlit interface further simplifies access to this technology, empowering farmers, agronomists, and researchers to make timely and informed decisions in precision agriculture.

 ---  

