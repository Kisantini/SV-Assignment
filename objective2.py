import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def show():
    st.title("Objective 2: Trends and Annual Changes (2018–2019)")
    st.write("""
    **Goal:** To analyze the annual change in rape rate and total cases across Indian states between 2018 and 2019.
    """)

    @st.cache_data
    def load_data():
        df = pd.read_csv("Rape cases dataset.csv")
        df.columns = df.columns.str.strip()
        return df

    df = load_data()

    # Bar Chart – Annual Change in Rape Rate
    st.subheader("1️⃣ Annual Change in Rape Rate by State (2018–2019)")
    fig4 = px.bar(df, x="State/UT", y="Annual Change in Rape Rate (2018-19)",
                  color="Annual Change in Rape Rate (2018-19)",
                  title="Annual Change in Rape Rate (2018–2019)")
    st.plotly_chart(fig4, use_container_width=True)

    # Scatter Plot – Rate vs Case Change
    st.subheader("2️⃣ Change in Cases vs Change in Rape Rate")
    fig5 = px.scatter(df, x="Annual Change in Cases (2018-19)",
                      y="Annual Change in Rape Rate (2018-19)",
                      text="State/UT", color="Annual Change in Rape Rate (2018-19)",
                      title="Change in Cases vs Rape Rate (2018–2019)")
    st.plotly_chart(fig5, use_container_width=True)

    # Heatmap – Correlation
    st.subheader("3️⃣ Correlation Heatmap")
    fig6, ax = plt.subplots()
    sns.heatmap(df[["2019 Rape Rate (per 100k pop)", 
                    "Annual Change in Rape Rate (2018-19)", 
                    "Annual Change in Cases (2018-19)"]].corr(),
                annot=True, cmap="coolwarm", fmt=".2f")
    st.pyplot(fig6)
