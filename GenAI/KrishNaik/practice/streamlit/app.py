import streamlit as st
import pandas as pd
import numpy as np

st.title("StreamLite App")
st.text("This app is for development purpose")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.write("Dummy Data..")
st.write(df)

st.write("Dummy Chart..")
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=['a','b','c']
)
st.line_chart(chart_data)
st.bar_chart(chart_data)
