
import pandas as pd 
from geopy.geocoders import Nominatim
import os 
import re
import numpy as np



#https://stackoverflow.com/questions/31414481/new-column-with-coordinates-using-geopy-pandas
#https://github.com/plotly/dash-phylogeny/blob/8b4a4ebb66238ee2b983281b8ab96ed81a434ece/generation_stat.py#L45



def get_coordinates(City):
       
    geolocator = Nominatim(user_agent = "Crime_flask_uni")
    
    try:
        location = geolocator.geocode(City)
        return [location.latitude, location.longitude]
    except AttributeError:
        return [0, 0]
    

def get_heatmap():
    
    coords = []
    df_path = r"D:\Programming\Crime_flask_uni\Crime_flask_uni\processing\Crime_stats_scotland.csv"
    try:
        df = pd.read_csv(df_path)
        unique_cities = df['FeatureName'].drop_duplicates().dropna()
        for city in unique_cities:
            coord = get_coordinates(city)
            if coord:
                coords.append(coord)
        return coords
    
    except Exception as e:
        print(f" processing error {e}")
        return []
    


