import streamlit as st
import pandas as pd

def show():
    st.title("🏠 Home – Rape Cases in India (2019)")

    st.write("""
    Welcome to the **Scientific Visualization Dashboard** for Rape Case Analysis (2019).  
    This app visualizes and interprets data trends across Indian states using scientific visualization techniques.
    """)

    @st.cache_data
    def load_data():
        df = pd.read_csv("Rape cases dataset.csv")
        df.columns = df.columns.str.strip()
        return df

    df = load_data()
    st.subheader("📘 Dataset Overview")
    st.dataframe(df)
    st.write(f"**Total Records:** {df.shape[0]} | **Columns:** {df.shape[1]}")

    st.info("""
    ### Navigation Guide:
    - **Objective 1:** Distribution of rape cases across states  
    - **Objective 2:** Yearly trends and rate changes (2018–2019)  
    - **Objective 3:** Correlation between rape cases and related crimes
    """)
