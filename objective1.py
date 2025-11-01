import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def show():
    st.title("Objective 1: Distribution of Rape Cases Across States (2019)")
    st.write("""
    **Goal:** To analyze the overall distribution of rape cases across Indian States and Union Territories in 2019 
    and to understand the demographic breakdown of adult and minor victims.
    """)

    # -----------------------------
    # Load Dataset
    # -----------------------------
    @st.cache_data
    def load_data():
        df = pd.read_csv("Rape cases dataset.csv")
        df.columns = df.columns.str.strip()
        return df

    df = load_data()

    # =============================
    # 1️⃣ Bar Chart – Top 10 States by Total Rape Cases
    # =============================
    st.subheader("1️⃣ Top 10 States by Total Rape Cases")
    top_states = df.sort_values(by="Total Rape Cases 2019", ascending=False).head(10)
    fig1 = px.bar(
        top_states,
        x="State/UT",
        y="Total Rape Cases 2019",
        color="Total Rape Cases 2019",
        text_auto=True,
        title="Top 10 States by Total Rape Cases (2019)"
    )
    fig1.update_layout(xaxis_title="State / UT", yaxis_title="Number of Cases")
    st.plotly_chart(fig1, use_container_width=True)
    st.caption("🔍 *The bar chart highlights that states like Rajasthan, Uttar Pradesh, and Madhya Pradesh reported the highest number of rape cases in 2019.*")

    # =============================
    # 2️⃣ Pie Chart – Adult vs Minor Victims (National Total)
    # =============================
    st.subheader("2️⃣ Proportion of Adult vs Minor Victims (India Total)")
    adult = df["Adult Cases (18+ yrs)"].sum()
    minor = df["Minor Cases (<18 yrs)"].sum()
    fig2 = px.pie(
        values=[adult, minor],
        names=["Adult Victims (18+)", "Minor Victims (<18)"],
        title="Overall Distribution of Victim Age Groups in 2019",
        color_discrete_sequence=["#ff6361", "#58508d"]
    )
    st.plotly_chart(fig2, use_container_width=True)
    st.caption("🔍 *Adults account for a larger share of victims nationwide, though minors still make up a concerning proportion.*")

    # =============================
    # 3️⃣ Histogram – Frequency of Rape Rates Across States
    # =============================
    st.subheader("3️⃣ Distribution of Rape Rate (per 100,000 Population)")
    fig3, ax = plt.subplots(figsize=(7, 4))
    sns.histplot(df["2019 Rape Rate (per 100k pop)"], bins=10, kde=True, color="#007acc", ax=ax)
    ax.set_xlabel()

