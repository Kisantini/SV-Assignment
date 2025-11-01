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

    # =============================
    # 3️⃣ Histogram – Frequency of Rape Rates Across States
    # =============================
    st.subheader("3️⃣ Distribution of Rape Rate (per 100,000 Population)")
    fig3, ax = plt.subplots(figsize=(7, 4))
    sns.histplot(
        df["2019 Rape Rate (per 100k pop)"],
        bins=10,
        kde=True,
        color="#007acc",
        ax=ax
    )
    ax.set_xlabel("Rape Rate per 100,000 Population")
    ax.set_ylabel("Number of States/UTs")
    ax.set_title("Distribution of Rape Rate Across States (2019)")
    st.pyplot(fig3)

    # =============================
    # 🧾 Summary Box
    # =============================
    st.subheader("📦 Summary Box")
    st.markdown("""
    <div style="background-color:#f7f7f9; padding:15px; border-radius:10px;">
    <p style="text-align:justify;">
    The analysis of rape case distribution in 2019 reveals clear regional and demographic trends. 
    The bar chart shows that northern and central states such as Rajasthan, Uttar Pradesh, and Madhya Pradesh 
    reported the highest number of cases, suggesting potential socio-economic and reporting differences across regions. 
    The pie chart indicates that adults constitute the majority of victims, accounting for roughly three-quarters of the total, 
    while minors still represent a significant fraction. 
    The histogram demonstrates that most states maintain relatively low rape rates per population, 
    but a few outliers show substantially higher rates. 
    Overall, these findings highlight disparities across states and emphasize the need for targeted awareness 
    and preventive initiatives.
    </p>
    </div>
    """, unsafe_allow_html=True)

    # =============================
    # 💬 Interpretation / Discussion
    # =============================
    st.subheader("💬 Interpretation / Discussion")
    st.write("""
    The visualizations clearly depict uneven distribution of rape cases across India.  
    States with higher populations and greater urban density—such as **Rajasthan, Madhya Pradesh, and Uttar Pradesh**—
    record the most cases, though not necessarily the highest rates when adjusted for population.  
    The pie chart emphasizes that **adult women (18+) are the most affected**, highlighting gender-based vulnerability 
    among adult populations.  
    The histogram distribution shows that most states have moderate rape rates, 
    but outliers such as **Assam and Delhi** exhibit disproportionately high rates relative to population.  
    These results imply that both **population structure and local socio-cultural conditions** 
    influence the frequency and reporting of rape incidents.  
    Policymakers should focus on awareness, education, and stricter law enforcement 
    in states displaying both high total and high relative rates.
    """)
