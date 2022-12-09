import pandas as pd
import numpy as np
import streamlit as st
import joblib

st.set_page_config(
    page_title="Site Energy Intensity Prediction",
    page_icon="⚡",
    layout="centered",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# feature list for prediction
feature_list = ['floor_area', 'energy_star_rating', 'ELEVATION', 'cooling_degree_days',
    'heating_degree_days', 'precipitation_inches', 'snowfall_inches',
    'days_above_80F', 'days_above_100F', 'max_wind_speed', 'days_with_fog',
    'Avg_min_temp_winter', 'Avg_max_temp_winter', 'Avg_temp_winter',
    'Avg_min_temp_summer', 'Avg_max_temp_summer', 'Avg_temp_summer',
    'Avg_days_below30F']

model = joblib.load("Site-Energy-Intensity-Prediction-Project\Models\eui_model.joblib")

# UI for single and batch prediction using streamlit expander

def single_prediction():
    pass

def batch_prediction():
    pass

def single_explainer():
    pass

def batch_explainer():
    # summary plot
    # decision plot
    pass

def display_shap_from_batch():
    pass

def main():
    # main inputs
    # model inference
    # prediction UI
    pass