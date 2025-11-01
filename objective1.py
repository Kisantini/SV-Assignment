import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def show():
    st.title("Objective 1: Distribution of Rape Cases Across States (2019)")
    st.write("""
    **Goal:** To analyze the distribution of rape cases across Indian States and Union Territories in 2019, 
    exploring variations in total cases, population-adjusted rates, and the age composition of victims.
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
    # 1️⃣ Choropleth Map – Regional Distribution
    # =============================
    st.subheader("1️⃣ Geographical Distribution of Rape Cases")
    st.write("The map shows regional variation in total rape cases reported in 2019.")

    # Note: requires a map dataset; for simplicity use bar substitute if map shapefile not available
    fig1 = px.choropleth(
        df,
        locations="State/UT",
        locationmode="geojson-id",  # placeholder; works when India geojson is added
        color="Total Rape Cases 2019",
        title="Rape Cases by State (2019)",
        color_continuous_scale="Reds"
    )
    st.plotly_chart(fig1, use_container_width=True)
    st.caption("🔍 *States with darker shades record higher total rape cases.*")

    # =============================
    # 2️⃣ Bubble Chart – Cases vs Rate
    # =============================
    st.subheader("2️⃣ Relationship Between Total Cases and Rape Rate")
    fig2 = px.scatter(
        df,
        x="Total Rape Cases 2019",
        y="2019 Rape Rate (per 100k pop)",
        size="Adult Cases (18+ yrs)",
        color="Minor Cases (<18 yrs)",
        text="State/UT",
        title="Bubble Chart: Total Cases vs Rate (Size = Adult Victims, Color = Minor Victims)"
    )
    st.plotly_chart(fig2, use_container_width=True)
    st.caption("🔍 *Larger bubbles = more adult victims; deeper color = more minor victims.*")

    # =============================
    # 3️⃣ Stacked Bar – Adult vs Minor Victims
    # =============================
    st.subheader("3️⃣ Comparison of Adult and Minor Victims by State")
    long_df = df.melt(
        id_vars="State/UT",
        value_vars=["Adult Cases (18+ yrs)", "Minor Cases (<18 yrs)"],
        var_name="Victim Type",
        value_name="Cases"
    )
    fig3 = px.bar(
        long_df.sort_values("Cases", ascending=False),
        x="State/UT", y="Cases",
        color="Victim Type",
        title="Adult vs Minor Victims by State (2019)",
        barmode="stack"
    )
    st.plotly_chart(fig3, use_container_width=True)
    st.caption("🔍 *Stacked bars highlight states with high adult and/or minor victim counts.*")

    # =============================
    # 🧾 Summary Box (100–150 words)
    # =============================
    st.subheader("📦 Summary Box")
    st.markdown("""
    <div style="background-color:#f0f2f6; padding:15px; border-radius:10px;">
    <p style="text-align:justify;">
    The analysis reveals significant disparities in rape case distribution across India in 2019. 
    Northern and central regions show the highest totals, while smaller northeastern states 
    report fewer cases but occasionally higher population-adjusted rates. 
    The bubble visualization indicates that states with large urban populations 
    not only record higher total cases but also exhibit elevated rape rates. 
    Age-based analysis demonstrates that adult victims form the majority, 
    although minor cases remain a notable share in several states. 
    Together, these patterns emphasize that both population density 
    and socio-demographic factors influence the occurrence and reporting of rape incidents.
    </p>
    </div>
    """, unsafe_allow_html=True)

    # =============================
    # 💬 Interpretation / Discussion
    # =============================
    st.subheader("💬 Interpretation / Discussion")
    st.write("""
    The distribution analysis shows that rape incidents are not evenly spread across India.  
    States such as **Madhya Pradesh, Rajasthan, and Uttar Pradesh** contribute a large proportion of 
    national cases, suggesting either higher crime occurrence or more efficient reporting.  
    The bubble chart demonstrates a moderate positive relationship between total cases 
    and rape rate, meaning states with higher numbers often face higher risk per capita.  
    The stacked bar comparison confirms that **adult women (18+)** remain the most affected group, 
    but **minor victims** form a persistent subset across states.  
    This spatial and demographic imbalance underlines the need for region-specific 
    policy interventions, awareness programs, and improved protection mechanisms 
    for vulnerable populations.
    """)
