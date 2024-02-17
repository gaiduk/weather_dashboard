import streamlit as st


st.title("Weather Forecast for the next days")
place = st.text_input("Place ")

days = st.slider("Forecast days")