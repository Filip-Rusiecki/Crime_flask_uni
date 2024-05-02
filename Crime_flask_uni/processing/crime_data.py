

import pandas as pd 
import numpy as np
import Crime_flask_uni.processing.geolocator as geo


def crime_all_data():
    df_path = r"D:\Programming\Crime_flask_uni\Crime_flask_uni\processing\Crime_stats_scotland_coords.csv"
    
    # Load the CSV data into a DataFrame
    all_data = pd.read_csv(df_path)
    
    
    return all_data


def crime_cities_coordinates():
    
    all_data = crime_all_data()
    
    heat_data = geo.get_heatmap()
    
    city_coordinates = pd.DataFrame({
         
        'FeatureLocation': ['Lat', 'Lng'],
            'lat': [56.4907, 56.5000],
            'lng': [-4.2026, -4.2100],
            
        })

    if heat_data:
        
        heat_data = np.array(heat_data)
                   
        heat_data_df = pd.DataFrame(heat_data, columns=["lat", "lng"])
        city_coordinates = city_coordinates.join(heat_data_df.set_index(["lat", "lng"]), on=['lat', 'lng'], how='outer')
        
        
        
    return city_coordinates
"""
def home():
    
    all_data = crime.crime_data_offence_date()


    
    ## Create a map object
   
 
    map = folium.Map(location=[56.4907, -4.2026], zoom_start=7,width=500,height=400)    
    
    heat_data = geo.get_heatmap()
    
    all_loc = pd.DataFrame({

        'FeatureLocation': ['Location1', 'Location2'],
            'lat': [56.4907, 56.5000],
            'lng': [-4.2026, -4.2100],
            
        })

    
    if heat_data:
        #folium.plugins.HeatMap(heat_data).add_to(map)

        ## add heat_data to all_data dataframe , heat_data cannot contain NaN values
        
        heat_data = np.array(heat_data)
        
              
        heat_data_df = pd.DataFrame(heat_data, columns=["lat", "lng"])
        all_data = all_data.join(heat_data_df.set_index(["lat", "lng"]), on=['lat', 'lng'], how='outer')
        
        if 'lat' in all_data.columns and 'lng' in all_data.columns:
                
                all_data = all_data.join(heat_data_df.set_index(['lat', 'lng']), on=['lat', 'lng'], how='outer')
        else:
            return "Error: 'lat' and 'lng' columns are required in all_data"

        if 'lat' in all_data.columns and 'lng' in all_data.columns:    
            
            for index, row in all_data.iterrows():             
                popup_text = all_data              
                folium.Marker([row['lat'], row['lng']], popup=popup_text).add_to(map)
        else:
            return "Error: 'lat' and 'lng' columns are required for placing markers"
      
    return  map._repr_html_(), render_template("index.html",data=all_data)
"""