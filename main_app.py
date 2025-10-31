import streamlit as st
import home
import objective1
import objective2
import objective3

# Page setup
st.set_page_config(page_title="Rape Cases Visualization", layout="wide")

# Sidebar
st.sidebar.title("📊 Navigation Menu")
page = st.sidebar.radio(
    "Select a page:",
    ("Home", "Objective 1", "Objective 2", "Objective 3")
)

# Routing (call the right page)
if page == "Home":
    home.show()
elif page == "Objective 1":
    objective1.show()
elif page == "Objective 2":
    objective2.show()
elif page == "Objective 3":
    objective3.show()
