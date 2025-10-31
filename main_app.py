import streamlit as st
import Home
import Objective1
import Objective2
import Objective3

# Set up page configuration
st.set_page_config(page_title="Rape Cases in India (2019)", layout="wide")

# Sidebar menu
st.sidebar.title("📊 Navigation Menu")
menu = st.sidebar.radio(
    "Go to",
    ["Home", "Objective 1", "Objective 2", "Objective 3"]
)

pg.run
