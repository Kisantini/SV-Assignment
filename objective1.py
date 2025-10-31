import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.title("Objective 1: Distribution of Rape Cases Across States (2019)")
    st.write("""
    **Goal:** To understand how rape cases are distributed across different states 
    and age groups in India.
    """)

    @st.cache_data
    def load_data():
        df = pd.read_csv("Rape cases dataset.csv")
        df.columns = df.columns.str.strip()
        return df

    df = load_data()

    # Bar Chart – Top 10 States
    st.subheader("1️⃣ Top 10 States by Total Rape Cases")
    top_states = df.sort_values(by="Total Rape Cases 2019", ascending=False).head(10)
    fig1 = px.bar(top_states, x="State/UT", y="Total Rape Cases 2019",
                  color="Total Rape Cases 2019", title="Top 10 States by Total Rape Cases (2019)")
    st.plotly_chart(fig1, use_container_width=True)

    # Pie Chart – Adult vs Minor
    st.subheader("2️⃣ Proportion of Adult vs Minor Victims")
    adult = df["Adult Cases (18+ yrs)"].sum()
    minor = df["Minor Cases (<18 yrs)"].sum()
    fig2 = px.pie(values=[adult, minor], names=["Adult Victims (18+)", "Minor Victims (<18)"],
                  title="Adult vs Minor Victims (India, 2019)")
    st.plotly_chart(fig2, use_container_width=True)

    # Scatter Plot – Rate vs Cases
    st.subheader("3️⃣ Rape Rate vs Total Cases by State")
    fig3 = px.scatter(df, x="Total Rape Cases 2019",
                      y="2019 Rape Rate (per 100k pop)",
                      text="State/UT", color="2019 Rape Rate (per 100k pop)",
                      title="Rape Rate vs Total Cases (2019)")
    st.plotly_chart(fig3, use_container_width=True)
