"""
Routes and views for the flask application.
"""

from datetime import datetime
from turtle import fillcolor
from flask import render_template
from Crime_flask_uni import app
from flask import Flask
import requests 
import folium
import pandas as pd
import streamlit as st
import numpy as np
from folium import GeoJson, Popup, plugins
import geojson
from datetime import datetime, timedelta
import Crime_flask_uni.processing.geolocator as geo
import Crime_flask_uni.processing.crime_data as crime


@app.route('/',methods=["GET"])





def home():
    
    all_data = crime.crime_all_data()
    coordinates = crime.crime_cities_coordinates()


    map = folium.Map(location=[56.4907, -4.2026], zoom_start=7,width=500,height=400)    

    if 'lat' in coordinates.columns and 'lng' in coordinates.columns:    
            
                for index, row in coordinates.iterrows():             
                                
                    folium.Marker([row['lat'], row['lng']], popup="popup_text").add_to(map)
    else:
           return "Error: 'lat' and 'lng' columns are required for placing markers"   
                  
      
    return  map._repr_html_(), render_template("index.html",data=all_data)


if __name__ == "__main__":
    app.run(debug=True)



