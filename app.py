import pandas as pd
import numpy as np
import streamlit as st
import joblib
import matplotlib.pyplot as plt
import shap
from IPython import get_ipython
from PIL import Image
import xgboost 
from styles import *

streamlit_style()

# feature list for prediction
feature_list = ['floor_area', 'energy_star_rating', 'ELEVATION', 'cooling_degree_days',
    'heating_degree_days', 'precipitation_inches', 'snowfall_inches',
    'days_above_80F', 'days_above_100F', 'max_wind_speed', 'days_with_fog',
    'Avg_min_temp_winter', 'Avg_max_temp_winter', 'Avg_temp_winter',
    'Avg_min_temp_summer', 'Avg_max_temp_summer', 'Avg_temp_summer',
    'Avg_days_below30F']

# https://xgboost.readthedocs.io/en/latest/tutorials/saving_model.html  (for model saving)

#model = xgb.Booster().load_model("./Models/site_eui_model.json")
model = joblib.load("./Models/eui_model.joblib")

# UI for single and batch prediction using streamlit expander

def single_prediction(features_val):
    values = np.array(features_val).reshape(1,-1)
    prediction = model.predict(values)
    pred = list(prediction)[0]
    return pred

def batch_prediction(df):
    n_df = df.iloc[:,1:]
    batch_preds = model.predict(n_df)
    pred_df = pd.DataFrame({'Site namees':df.iloc[:,0], 'EUI_prediction':batch_preds})
    st.success("Results sucessfully generated!")
    _, x2, x3, _ = st.columns([0.1, 0.4, 0.4, 0.1], gap = 'medium')
    with x2:
        st.markdown("<h4 style='text-align: left; color: #e3a740;'>Site EUI Predictions</h4>",
                unsafe_allow_html = True)
        st.dataframe(pred_df)
    
    with x3:
        st.markdown("<h4 style='text-align: left; color: #e3a740;'>Sorted EUI Predictions</h4>",
                unsafe_allow_html = True)
        sorted_df = pred_df.sort_values(by='EUI_prediction', ascending=False)
        st.dataframe(sorted_df)
    st.write(" ")
    batch_explainer(n_df)
    st.write(" ")
        

def single_explainer(features_val):
    st.markdown("<h5 style='text-align: center; padding: 12px;color: #e3a740;'>Model Explanation : XAI (Explainable AI)</h5>",
                            unsafe_allow_html = True)  
    svalues = np.array(features_val).reshape(1,-1)  
    shap.initjs()
    shap_values = shap.TreeExplainer(model).shap_values(svalues)
    st.pyplot(shap.force_plot(shap.TreeExplainer(model).expected_value[0], shap_values[0], svalues, matplotlib=True,show=False))

def batch_explainer(df):
    y1, y2, y3 = st.columns([0.1, 0.8, 0.1])
    with y2:
        st.markdown("<h4 style='text-align: center; padding: 12px;color: #e3a740;'>Model Explanation : XAI (Explainable AI)</h4>",
                    unsafe_allow_html = True)
        # summary plot
        shap_values = shap.TreeExplainer(model).shap_values(df)
        st.pyplot(shap.summary_plot(shap_values, df, plot_type='bar')) 
        st.write(" ")   
        # decision plot
        st.pyplot(shap.summary_plot(shap_values, df))

def display_shap_from_batch(df, name):
    st.markdown("<h5 style='text-align: center; padding: 12px;color: #4f4f4f;'>Model Explanation : XAI (Explainable AI)</h5>",
                unsafe_allow_html = True)
    temp = df.loc[df['name'] == name]
    res = temp.iloc[:, 1:]
    shap.initjs()              
    shap_values = shap.TreeExplainer(model).shap_values(res)              
    st.pyplot(shap.force_plot(shap.TreeExplainer(model).expected_value[0], shap_values[0], res, matplotlib=True,show=False))

def main():
    # main inputs
    heading = '''
                <div> 
                <h1 style ="color:#db9112;text-align:center;padding:25px;">Site Energy Intensity Prediction App</h1> 
                </div> 
            '''
    st.markdown(heading, unsafe_allow_html = True)
    st.write("")
    image = Image.open("./Images/examples-renewable-energy-wind-solar-biomass-geothermal.jpg")
    
    p,q,r = st.columns(3)
    with q:
        st.image(image, caption="Green Building Image")
        
    st.write(" ")
    
    with st.expander("Site EUI prediction"):
        x, y = st.columns(2, gap='medium')
        with x:
            st.header("Building characteristics")
            floor_area = st.number_input("Floor area", step=1)
            star_ratings = st.number_input("Energy star ratings", step=1)
            elevation = st.number_input("Elevation of a building", step=1)
            
            image2 = Image.open("./Images/Explain-scientific-solutions-to-help-industries-reduce-their-energy-consumption.webp")
            st.write(" ")
            st.image(image2)
            st.write(" ")
            st.markdown("""
                        <div> 
                        <h5 style ="color:#4f4f4f;text-align:center;padding:25px;">Save energy, Save earth</h5> 
                        </div> 
                        """, unsafe_allow_html = True)
        with y:
            st.header("Site weather conditions")
            cdd = st.number_input('Cooling degree days', step=1)
            hdd = st.number_input('Heating degree days', step=1)
            precipitation = st.number_input('Precipitation inches', step=1)
            snowfall = st.number_input('Snowfall inches', step=1)
            days_above_80F = st.number_input('Days above 80F', step=1)
            days_above_100F = st.number_input('Days above 100F', step=1)
            max_wind_speed = st.number_input('Max wind speed', step=1)
            days_with_fog = st.number_input('Days with fog', step=1)
            avg_min_winter = st.slider('Average min winter temp(in F)',0,100,step=1)
            avg_max_winter = st.slider('Average max winter temp(in F)', 0,100,step=1)
            avg_winter = st.slider('Average winter temp(in F)', 0,100,step=1)
            avg_min_sum = st.slider('Average min summer temp(in F)', 0,100,step=1)
            avg_max_sum = st.slider('Average max summer temp(in F)', 0,100,step=1)
            avg_sum = st.slider('Average summer temp(in F)', 0,100,step=1)
            avg_days_b30F = st.slider('Average days below 30F', 0,100,step=1)
        
        features_names = ['floor_area', 'energy_star_rating', 'ELEVATION', 'cooling_degree_days',
                        'heating_degree_days', 'precipitation_inches', 'snowfall_inches',
                        'days_above_80F', 'days_above_100F', 'max_wind_speed', 'days_with_fog',
                        'Avg_min_temp_winter', 'Avg_max_temp_winter', 'Avg_temp_winter',
                        'Avg_min_temp_summer', 'Avg_max_temp_summer', 'Avg_temp_summer',
                        'Avg_days_below30F']
        features_values = [floor_area,star_ratings,elevation,cdd,hdd,precipitation,snowfall,days_above_80F,
                        days_above_100F,max_wind_speed,days_with_fog,avg_min_winter,
                        avg_max_winter,avg_winter,avg_min_sum,avg_max_sum,avg_sum,avg_days_b30F]
        lst = []
        for i in features_values[:11]:
            if i != 0:
                lst.append(True)
        if False in lst:
            st.write("Please enter the correct input values")
        else:
            result = single_prediction(features_values)
            st.write("Click below to predit site EUI")
            if st.button("Predict"):
                st.markdown(f"**Site energy usage intensity is {result}** units")
                
                single_explainer(features_values)
            
    with st.expander("Batch of site prediction"):
        uploader = st.file_uploader("Upload the batch of sites datasheet")
        if uploader:
            df = pd.read_excel(uploader)
            batch_prediction(df)
            names = tuple(df['name'])
            
            st.write(" ")
            st.markdown("<h4 style='text-align: center; padding: 12px;color: #e3a740;'>Single Patient Model Explanation</h4>",
                        unsafe_allow_html = True)
            single_patient = st.selectbox('Select Patient', names)
            st.write(" ")

            if st.button("Explain"):
                display_shap_from_batch(df, single_patient)       
                
if __name__=='__main__': 
    main()
    
    st.write("Developed By: Avi kumar Talaviya")
    st.markdown("""Reach out to me on: [Twitter](https://twitter.com/avikumart_) |
            [Linkedin](https://www.linkedin.com/in/avi-kumar-talaviya-739153147/) |
            [Kaggle](https://www.kaggle.com/avikumart) 
            """)
    
