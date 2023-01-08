import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("em yeu")

st.title('The Titanic dataset')
df = pd.read_csv("second.csv")

st.subheader("The data")
st.write(df)

st.subheader("Some visualizations")
