# Weather-Info-Web-and-Streamlit

## Overview
The Weather Information App is a web application that provides users with the latest weather details for any specified city. It utilizes the WeatherStack API to fetch real-time weather data, including temperature, humidity, wind speed, and more. The app has two components: a Python-based backend using Streamlit and a front-end interface built with HTML, CSS, and JavaScript.

## Features
- Real-time weather updates for any city.
- Displays temperature, humidity, wind speed, pressure, and more.
- Provides an easy-to-use interface.
- Fetches and displays weather icons.

## Components

### 1. Streamlit Application (Python)
- **Backend**: Built using Python and Streamlit.
- **Functionality**:
  - Fetches weather data from the WeatherStack API.
  - Displays weather information in a well-organized layout.
  - Customizable background and styles.

### 2. Frontend (HTML, CSS, JavaScript)
- **Frontend Interface**: Designed using HTML and styled with CSS.
- **Interactivity**: JavaScript is used to fetch data and dynamically update the UI.

## Prerequisites

### For Streamlit Application:
- Python 3.x
- Streamlit
- Requests
- Pillow

### For Frontend:
- Basic understanding of HTML, CSS, and JavaScript.

## Installation and Usage

### Running the Streamlit App:
1. Clone the repository.
2. Navigate to the project directory.
3. Install the required Python packages:
   ```bash
   pip install streamlit requests Pillow
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
5. Open your web browser and go to `http://localhost:8501` to view the app.

### Running the Frontend (index.html):
1. Clone the repository.
2. Open `index.html` in a web browser.

## Configuration
- Replace the `access_key` variable with your own WeatherStack API key in both the Streamlit app (`app.py`) and the frontend JavaScript.

```

## Detailed Description

### app.py
The Streamlit app (`app.py`) is the backend that fetches weather data from the WeatherStack API and displays it in a user-friendly format.

Key functions:
- `get_weather(location, access_key)`: Fetches weather data for the specified location.
- `get_weather_icon(icon_url)`: Downloads and returns the weather icon from the given URL.
- `main()`: Main function that defines the Streamlit interface and handles user interactions.

### index.html
The `index.html` file is the frontend interface that users can access directly. It fetches weather data using JavaScript and displays it on the webpage.

Key sections:
- Input field for city name.
- Button to fetch weather information.
- Display area for weather details including temperature, humidity, wind speed, and more.

### Styles and Scripts
- **CSS**: Used for styling the web interface, including background colors, fonts, and layout.
- **JavaScript**: Handles API requests and dynamically updates the webpage content based on user input.

## How to Use
1. **Using the Streamlit App**:
   - Open the Streamlit app.
   - Enter the city name in the text input field.
   - Click on the "Get Weather" button to fetch and display the weather information.

2. **Using the Frontend Interface**:
   - Open `index.html` in a web browser.
   - Enter the city name in the input field.
   - Click the "Get Weather" button to fetch and display the weather information.

## API Reference
This app uses the WeatherStack API to fetch weather data. For more details on the API, visit [WeatherStack API Documentation](https://weatherstack.com/documentation).

## Acknowledgments
- [Streamlit](https://streamlit.io/) for the easy-to-use framework.
- [WeatherStack](https://weatherstack.com/) for providing the weather data API.
- Inspired by various online tutorials and resources.

