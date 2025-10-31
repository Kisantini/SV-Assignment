import streamlit as st
import pandas as pd

st.set_page_config(page_title="Rape Cases in India (2019)", layout="wide")

st.title("📊 Rape Cases in India (2019) – Scientific Visualization Project")

st.write("""
Welcome to the Streamlit dashboard for the analysis of **Rape Cases in India (2019)**.  
This application demonstrates the use of **scientific visualization techniques** to explore data patterns, 
compare trends, and interpret correlations among key indicators.
""")

st.subheader("📘 About the Dataset")
st.write("""
- **Source:** Open statistical data (derived from NCRB, India)
- **Records:** 37 (India + 36 States/UTs)
- **Year:** 2019
- **Key Attributes:** Total cases, age-wise distribution, rate per 100k population, 
  annual changes, and related crimes (Kidnapping/Abduction under IPC 366)
""")

st.info("""
Use the **sidebar** or top navigation to explore the following objectives:
1️⃣ Distribution of Rape Cases  
2️⃣ Trends and Rate Changes (2018–2019)  
3️⃣ Correlation with Related Crimes  
""")

# Preview dataset
@st.cache_data
def load_data():
    df = pd.read_csv("Rape cases dataset.csv")
    df.columns = df.columns.str.strip()
    return df

df = load_data()
st.dataframe(df)
st.write(f"**Total Records:** {df.shape[0]} | **Columns:** {df.shape[1]}")
