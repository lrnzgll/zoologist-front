import requests
import streamlit as st

"""
# Zoologist front
"""

island = st.radio('Select an Island', ('Biscoe', 'Dream', 'Torgersen'))

st.write('The island is ', island)

bill_length = st.number_input('Bill length (in mm)')

st.write('The bill length is ', bill_length)

bill_depth = st.number_input('Bill depth (in mm)')

st.write('The bill depth is ', bill_depth)

flipper_length = st.number_input('flipper length(in mm)')

st.write('The flipper length is ', flipper_length)

body_mass = st.number_input('body mass (in mm)')

st.write('The body mass is ', body_mass)

sex = st.radio('Select an Island', ('Male', 'Female'))

st.write(sex)

api_url = st.secrets['API_URL']

params = {
    "island": island,
    "bill_length_mm": bill_length,
    "bill_depth_mm": bill_depth,
    "flipper_length_mm": flipper_length,
    "body_mass_g": body_mass,
    "sex": sex
}

if st.button('Predict penguin class'):
    response = requests.get(api_url, params)
    prediction = response.json()
    st.write("The predicted penguin class is", prediction)
