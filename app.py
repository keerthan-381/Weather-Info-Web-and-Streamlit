import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Function to fetch weather data
def get_weather(location, access_key):
    url = f"http://api.weatherstack.com/current"
    params = {
        'access_key': access_key,
        'query': location
    }
    response = requests.get(url, params=params)
    return response.json()

# Function to fetch weather icon (WeatherStack returns an icon URL)
def get_weather_icon(icon_url):
    response = requests.get(icon_url)
    img = Image.open(BytesIO(response.content))
    return img

# Streamlit app interface
def main():
    # Set a custom background image or color
    st.markdown("""
        <style>
        .reportview-container {
            background-size: cover;
        }
        .sidebar .sidebar-content {
            background-color: #0e1a2b;
        }
        .stButton>button {
            background-color: #1e90ff;
            color: white;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

    # App title with large font size and color
    st.title("🌤️ Weather Information App")
    st.markdown("Get the latest weather information, including temperature, humidity, wind speed, and more!")

    # Input for location
    location = st.text_input("Enter the city name", "New York")

    # Button to get weather
    if st.button("Get Weather", key="get_weather"):
        # Your WeatherStack access key
        access_key = 'YOUR_API_KEY'

        # Fetch the weather data
        weather_data = get_weather(location, access_key)

        # Check if the request was successful
        if 'error' in weather_data:
            st.error("Error: " + weather_data['error']['info'])
        else:
            # Display weather information in columns for better layout
            location_data = weather_data['location']
            current_weather = weather_data['current']

            # Display the location name and country
            st.subheader(f"Weather in {location_data['name']}, {location_data['country']}")
            st.caption(f"Observation Time: {current_weather['observation_time']}")


            # Layout the weather data in two columns
            col1, col2 = st.columns(2)

            # Column 1: Temperature and Weather Description
            with col1:
                st.write(f"**Temperature**: {current_weather['temperature']}°C")
                st.write(f"**Weather Description**: {', '.join(current_weather['weather_descriptions'])}")

            # Column 2: Wind and Pressure Data
            with col2:
                st.write(f"**Wind Speed**: {current_weather['wind_speed']} km/h")
                st.write(f"**Wind Direction**: {current_weather['wind_dir']}")
                st.write(f"**Pressure**: {current_weather['pressure']} hPa")

            # Column 1: Precipitation and Humidity
            with col1:
                st.write(f"**Precipitation**: {current_weather['precip']} mm")
                st.write(f"**Humidity**: {current_weather['humidity']}%")

            # Column 2: Visibility and Wind Degree
            with col2:
                st.write(f"**Wind Degree**: {current_weather['wind_degree']}°")
                st.write(f"**Visibility**: {current_weather['visibility']} km")

            # Add a footer
            st.markdown("---")
            st.markdown("Made with ❤️ using [Streamlit](https://www.streamlit.io/)")

if __name__ == "__main__":
    main()
