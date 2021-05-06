# -*- coding: utf-8 -*-
"""
Application File for Streamlit App for NLP APP
"""
import streamlit as st
from tensorflow import keras

mod = keras.models.load_model('nlp_model')

st.title("NLP Sentiment Analysis")
text = st.text_area("Please Enter Your Text for Sentiment Analysis")

if text:
    prediction = mod.predict([text])[0][0]
    
    if prediction > 0.5:
        sentiment = 'Positive'
    else:
        sentiment = 'Negative'
        prediction = 1 - prediction
else:
    prediction = None
    
if prediction:
    st.header(f"Estimated Sentiment: {sentiment}, With Probability: {prediction}")
else:
    st.header("Please enter text in order to get a prediction on sentiment.")


