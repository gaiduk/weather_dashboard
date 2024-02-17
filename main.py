import streamlit as st
import plotly.express as px

import backend
from backend import get_data


st.title("Weather Forecast for the next days")
place = st.text_input("Place ")

days = st.slider("Forecast days", min_value=1, max_value=5,
                 help="Select a number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    filtered_data = get_data(place, days)

    if option == "Temperature":
        temperatures = [(int(dict["main"]["temp"]) - 273.15) for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperatures, labels={"x": "Dates", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png",
                  "Snow": "images/snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        images_path = [images[condition] for condition in sky_conditions]
        st.image(images_path, width=110)