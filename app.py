import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title='Weather App', page_icon='☀️')

st.title('🌤️Weather App')

st.write('Enter the city name and click on the button to get weather data')

city = st.text_input('Enter the city name')

API_KEY = os.getenv('API_KEY')
API_URL = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

if st.button('Fetch Weather Data'):
    response = requests.get(API_URL.format(city=city, API_KEY=API_KEY))
    data = response.json()
    if data['cod'] == 200:
     st.success('Weather data fetched successfully!')
    else:
        st.error('City not found. Please enter a valid city name.') 

    #Extract the values 
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    weather = data['weather'][0]['main']
    name = data['name']
    country = data['sys']['country']

    st.subheader(f'{name}, {country}')

    #Create 4 columns
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    # Display the values in UI
    col1.metric('Temperature', f'🌡️{temperature} °C')
    col2.metric('Humidity', f'💦{humidity} %')
    col3.metric('Wind Speed', f'🍃{wind_speed} m/s')
    col4.metric('Weather', f'☁️{weather}')

