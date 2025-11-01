import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def show():
    st.title("Objective 2: Annual Change and Trend Analysis (2018–2019)")
    st.write("""
    **Goal:** To study the yearly change in rape cases and rape rates between 2018 and 2019 
    and identify which states experienced increases or decreases in reported incidents.
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
    # 1️⃣ Line Chart – Annual Change in Rape Rate
    # =============================
    st.subheader("1️⃣ Annual Change in Rape Rate by State (2018–2019)")
    sorted_df = df.sort_values(by="Annual Change in Rape Rate (2018-19)", ascending=False)
    fig1 = px.line(
        sorted_df,
        x="State/UT",
        y="Annual Change in Rape Rate (2018-19)",
        markers=True,
        title="Change in Rape Rate (2018–2019)"
    )
    fig1.update_layout(xaxis_title="State / UT", yaxis_title="Rate Change (per 100,000 population)")
    st.plotly_chart(fig1, use_container_width=True)
    st.caption("🔍 *Positive values indicate a rise in rape rate; negative values indicate a decrease.*")

    # =============================
    # 2️⃣ Scatter Plot – Change in Cases vs Change in Rape Rate
    # =============================
    st.subheader("2️⃣ Relationship Between Case Change and Rate Change")
    fig2 = px.scatter(
        df,
        x="Annual Change in Cases (2018-19)",
        y="Annual Change in Rape Rate (2018-19)",
        text="State/UT",
        color="2019 Rape Rate (per 100k pop)",
        size="Total Rape Cases 2019",
        title="Scatter: Annual Change in Case Numbers vs Rate Change"
    )
    fig2.update_layout(xaxis_title="Change in Total Cases (2018–2019)", yaxis_title="Change in Rape Rate")
    st.plotly_chart(fig2, use_container_width=True)
    st.caption("🔍 *States with large increases in total cases often show parallel increases in rape rates.*")

    # =============================
    # 3️⃣ Correlation Heatmap – Relationship Among Key Indicators
    # =============================
    st.subheader("3️⃣ Correlation Among Key Indicators")
    corr_cols = [
        "2019 Rape Rate (per 100k pop)",
        "Annual Change in Rape Rate (2018-19)",
        "Annual Change in Cases (2018-19)"
    ]
    fig3, ax = plt.subplots(figsize=(6, 4))
    sns.heatmap(df[corr_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
    ax.set_title("Correlation Heatmap: Rate and Case Changes (2018–2019)")
    st.pyplot(fig3)
    st.caption("🔍 *Positive correlation shows that case count changes and rate changes are strongly related across states.*")

    # =============================
    # 🧾 Summary Box (100–150 words)
    # =============================
    st.subheader("📦 Summary Box")
    st.markdown("""
    <div style="background-color:#f7f7f9; padding:15px; border-radius:10px;">
    <p style="text-align:justify;">
    The trend analysis for 2018–2019 reveals varied changes in rape rates across Indian states. 
    Some regions, such as Rajasthan and Assam, experienced slight increases in both total cases and rate per population, 
    indicating continued vulnerability. Others, such as Andhra Pradesh and Gujarat, showed mild improvements, 
    suggesting enhanced preventive actions or underreporting. 
    The scatter plot confirms a positive correlation between annual change in case numbers 
    and rate change — states with more new cases also show greater rate increases. 
    The correlation heatmap reinforces this link, highlighting that the rate of occurrence 
    tends to rise proportionally with the absolute case count. 
    These findings illustrate the interconnected nature of case volume and rate trends across regions.
    </p>
    </div>
    """, unsafe_allow_html=True)

    # =============================
    # 💬 Interpretation / Discussion
    # =============================
    st.subheader("💬 Interpretation / Discussion")
    st.write("""
    The analysis clearly shows that rape rate changes are closely tied to total case variations across states.  
    Most regions experienced only minor fluctuations between 2018 and 2019, 
    but some states such as **Rajasthan, Madhya Pradesh, and Assam** reported notable increases, 
    reflecting both rising incidents and possibly better reporting mechanisms.  
    On the other hand, states with negative rate change values indicate improvement, 
    which could result from successful awareness campaigns or reporting inconsistencies.  
    The correlation heatmap further validates that **states with a higher surge in total cases 
    tend to show proportional increases in population-adjusted rates**.  
    These insights suggest that policy responses must combine both **law enforcement and community education**, 
    especially in states where both metrics have simultaneously increased.
    """)
