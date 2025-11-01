import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def show():
    st.title("Objective 3: Correlation Between Rape Cases and Related Crimes")
    st.write("""
    **Goal:** To explore the relationship between rape cases and related crimes such as 
    kidnapping or abduction for marriage (IPC 366) across Indian states. 
    This helps identify whether states with higher rape incidences also report 
    higher occurrences of these associated crimes.
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
    # 1️⃣ Scatter Plot – Rape Cases vs Kidnapping (IPC 366)
    # =============================
    st.subheader("1️⃣ Rape Cases vs Kidnapping for Marriage (IPC 366)")
    fig1 = px.scatter(
        df,
        x="Total Rape Cases 2019",
        y="Kidnapping/Abduction for Marriage (IPC 366)",
        color="2019 Rape Rate (per 100k pop)",
        size="Total Rape Cases 2019",
        text="State/UT",
        title="Relationship Between Rape Cases and Kidnapping for Marriage (IPC 366)"
    )
    fig1.update_layout(xaxis_title="Total Rape Cases (2019)", yaxis_title="Kidnapping/Abduction for Marriage (Cases)")
    st.plotly_chart(fig1, use_container_width=True)
    st.caption("🔍 *A visible upward trend shows that states with more rape cases tend to have higher kidnapping incidents too.*")

    # =============================
    # 2️⃣ Bar Chart – Related Crimes by Top 10 States
    # =============================
    st.subheader("2️⃣ Comparison of Related Crimes Among Top 10 States")
    top10 = df.sort_values(by="Total Rape Cases 2019", ascending=False).head(10)
    fig2 = px.bar(
        top10,
        x="State/UT",
        y="Kidnapping/Abduction for Marriage (IPC 366)",
        color="Kidnapping/Abduction for Marriage (IPC 366)",
        text_auto=True,
        title="Top 10 States: Kidnapping and Abduction for Marriage Cases (2019)"
    )
    fig2.update_layout(xaxis_title="State / UT", yaxis_title="Number of Kidnapping/Abduction Cases")
    st.plotly_chart(fig2, use_container_width=True)
    st.caption("🔍 *Rajasthan, Uttar Pradesh, and Bihar report both high rape and abduction rates, indicating related socio-legal issues.*")

    # =============================
    # 3️⃣ Correlation Heatmap – Relationship Among Key Indicators
    # =========
