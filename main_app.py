import streamlit as st
import Home
import Objective1
import Objective2
import Objective3

# Page setup
st.set_page_config(page_title="Rape Cases Visualization", layout="wide")

# Sidebar
st.sidebar.title("📊 Navigation Menu")
page = st.sidebar.radio(
    "Select a page:",
    ("Home", "Objective 1", "Objective 2", "Objective 3")
)

# Routing
if page == "Home":
    Home.show()
elif page == "Objective 1":
    Objective1.show()
elif page == "Objective 2":
    Objective2.show()
elif page == "Objective 3":
    Objective3.show()
