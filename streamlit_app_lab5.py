import streamlit as st
import requests

def get_current_weather(location, API_key):
    if "," in location:
        location = location.split(",")[0].strip()

    urlbase = "https://api.openweathermap.org/data/2.5/"
    urlweather = f"weather?q={location}&appid={API_key}"
    url = urlbase + urlweather
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        st.error(f"Error: {data.get('message', 'Something went wrong.')}")
        return None

    temp = data['main']['temp'] - 273.15
    feels_like = data['main']['feels_like'] - 273.15
    temp_min = data['main']['temp_min'] - 273.15
    temp_max = data['main']['temp_max'] - 273.15
    humidity = data['main']['humidity']

    return {
        "location": location,
        "temperature": round(temp, 2),
        "feels_like": round(feels_like, 2),
        "temp_min": round(temp_min, 2),
        "temp_max": round(temp_max, 2),
        "humidity": round(humidity, 2),
    }

def main():
    st.title("Weather Info App")

    location = st.text_input("Enter a location (e.g., 'Syracuse'):")
    API_key = st.secrets["OPENWEATHER_API_KEY"]

    if st.button("Get Weather"):
        if location and API_key:
            weather_data = get_current_weather(location, API_key)
            if weather_data:
                st.subheader(f"Weather in {weather_data['location']}")
                st.write(f"Temperature: {weather_data['temperature']}°C")
                st.write(f"Feels like: {weather_data['feels_like']}°C")
                st.write(f"Min Temperature: {weather_data['temp_min']}°C")
                st.write(f"Max Temperature: {weather_data['temp_max']}°C")
                st.write(f"Humidity: {weather_data['humidity']}%")
        else:
            st.error("Please enter both location and API key.")

if __name__ == "__main__":
    main()
