import streamlit as st
import pandas as pd

st.title("StreamLit Widgets")

st.write("Text Input")
name = st.text_input("Enter Your Name")
age = st.slider("Select your Age", 18, 100)

if name:
    st.write(f"Hi {name}")

if age:
    st.write(f"Your age is: {age}")

uploaded_file = st.file_uploader("Choose a CSV File", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df)