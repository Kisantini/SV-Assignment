import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------------
# PAGE CONFIGURATION
# ---------------------
st.set_page_config(page_title="Rape Statistics in India (2019)", layout="wide")

# ---------------------
# LOAD DATA
# ---------------------
@st.cache_data
def load_data():
    df = pd.read_csv("rape_statistics.csv")
    df.columns = df.columns.str.strip()  # Clean column names
    return df

df = load_data()

