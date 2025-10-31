import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def show():
    st.title("Objective 3: Correlation Between Rape Cases and Related Crimes")

    st.write("""
    **Goal:** To explore correlations between rape cases and related crimes such as 
    kidnapping or abduction for marriage (IPC 366).
    """)

    @st.cache_data
    def load_data():
        df = pd.read_csv("Rape cases dataset.csv")
        df.columns = df.columns.str.strip()
        return df

    df = load_data()

    # Scatter – Rape vs Kidnapping
    st.subheader("1️⃣ Rape Cases vs Kidnapping for Marriage (IPC 366)")
    fig7 = px.scatter(df, x="Total Rape Cases 2019",
                      y="Kidnapping/Abduction for Marriage (IPC 366)",
                      text="State/UT", color="Total Rape Cases 2019",
                      title="Rape Cases vs Kidnapping for Marriage (IPC 366)")
    st.plotly_chart(fig7, use_container_width=True)

    # Correlation Heatmap
    st.subheader("2️⃣ Correlation Heatmap of Crime Indicators")
    numeric_df = df.select_dtypes(include='number')
    fig8, ax = plt.subplots(figsize=(10, 5))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    st.pyplot(fig8)

    # Insights
    st.subheader("3️⃣ Observation Summary")
    st.info("""
    - States with higher rape cases tend to have higher kidnapping/abduction rates.
    - A positive correlation indicates overlapping socio-legal conditions.
    - Insights can inform policy interventions and awareness strategies.
    """)
