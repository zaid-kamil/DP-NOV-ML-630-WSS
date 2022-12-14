
import streamlit as st
from joblib import load
import numpy as np


def load_model(model_file):
    model = load(model_file)
    return model

def predict(model, sqrft=0, baths=0):
    x = np.array([[sqrft, baths]])
    y = model.predict(x)
    return y[0] # return first element of array

st.title("House Price Prediction")

with st.form(key='my_form'):
    sqrft = st.number_input(label='Square Feet', value=10000, min_value=100, 
    step=100)
    baths = st.number_input(label='Baths', value=2, min_value=1)
    submit_button = st.form_submit_button(label='Predict')

if submit_button:
    model = load_model('house_price.joblib')
    price = predict(model, sqrft, baths)
    st.success(f'Predicted price: {int(price):,}')