# vy_streamlit

https://donhuvy-vy-streamlit-streamlit-app-e4ydow.streamlit.app/

```python
!pip install streamlit
!pip install matplotlib
!pip install seaborn

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('The Titanic dataset')
df = pd.read_csv("second.csv")

st.subheader("The data")
st.write(df)

st.subheader("Some visualizations")
```
