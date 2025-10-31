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
    home.show()
elif page == "Objective 1":
    objective1.show()
elif page == "Objective 2":
    objective2.show()
elif page == "Objective 3":
    objective3.show()
