import pandas as pd
import numpy as np

# feature list for prediction
feature_list = ['floor_area', 'energy_star_rating', 'ELEVATION', 'cooling_degree_days',
    'heating_degree_days', 'precipitation_inches', 'snowfall_inches',
    'days_above_80F', 'days_above_100F', 'max_wind_speed', 'days_with_fog',
    'Avg_min_temp_winter', 'Avg_max_temp_winter', 'Avg_temp_winter',
    'Avg_min_temp_summer', 'Avg_max_temp_summer', 'Avg_temp_summer',
    'Avg_days_below30F']