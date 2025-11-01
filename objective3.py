import streamlit as st
import pandas as pd
import plotly.express as px

def show():
    st.title("Objective 3: Correlation Between Rape Cases and Related Crimes")
    st.write("""
    **Goal:** To understand the relationship between rape cases and related crimes such as 
    kidnapping or abduction for marriage (IPC 366) across Indian states. 
    The objective is to identify whether states with high rape incidences also show 
    higher levels of related crimes.
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
    # 1️⃣ Dual Bar Chart – Rape vs Kidnapping by State
    # =============================
    st.subheader("1️⃣ Comparison of Rape and Kidnapping Cases by State")
    sorted_df = df.sort_values(by="Total Rape Cases 2019", ascending=False)
    fig1 = px.bar(
        sorted_df,
        x="State/UT",
        y=["Total Rape Cases 2019", "Kidnapping/Abduction for Marriage (IPC 366)"],
        barmode="group",
        title="State-wise Comparison of Rape vs Kidnapping/Abduction Cases (2019)",
        labels={"value": "Number of Cases", "variable": "Crime Type"},
        color_discrete_sequence=["#ff6361", "#58508d"]
    )
    fig1.update_layout(
        xaxis_title="State / UT",
        yaxis_title="Number of Cases",
        legend_title_text="Crime Type",
        bargap=0.2
    )
    st.plotly_chart(fig1, use_container_width=True)
    st.caption("🔍 *The grouped bars make it easy to compare both crimes across states. States with higher rape cases also tend to have higher kidnapping/abduction cases.*")

    # =============================
    # 2️⃣ Horizontal Bar Chart – Compare Rape vs Kidnapping by State
    # =============================
    st.subheader("2️⃣ Comparison of Rape and Kidnapping Cases by State (Top 10)")
    top10 = df.sort_values(by="Total Rape Cases 2019", ascending=False).head(10)
    fig2 = px.bar(
        top10,
        y="State/UT",
        x=["Total Rape Cases 2019", "Kidnapping/Abduction for Marriage (IPC 366)"],
        orientation="h",
        barmode="group",
        title="Top 10 States: Rape vs Kidnapping/Abduction for Marriage Cases (2019)",
        labels={"value": "Number of Cases", "variable": "Crime Type"}
    )
    st.plotly_chart(fig2, use_container_width=True)
    st.caption("🔍 *This grouped bar chart makes it easy to compare both crimes side by side for each major state.*")

    # =============================
    # 3️⃣ Pie Chart – National-Level Proportion of Crimes
    # =============================
    st.subheader("3️⃣ Overall Proportion of Rape vs Kidnapping Cases in India (2019)")
    total_rape = df["Total Rape Cases 2019"].sum()
    total_kidnap = df["Kidnapping/Abduction for Marriage (IPC 366)"].sum()
    fig3 = px.pie(
        values=[total_rape, total_kidnap],
        names=["Total Rape Cases", "Kidnapping/Abduction (IPC 366)"],
        color_discrete_sequence=["#ff6361", "#58508d"],
        title="Overall Share of Rape and Kidnapping/Abduction Cases (2019)"
    )
    st.plotly_chart(fig3, use_container_width=True)
    st.caption("🔍 *Nationally, rape cases form a larger proportion, but kidnapping/abduction incidents also represent a major concern.*")

    # =============================
    # 🧾 Summary Box (Black Background)
    # =============================
    st.subheader("📦 Summary Box")
    st.markdown("""
    <div style="background-color:#1e1e1e; padding:15px; border-radius:10px;">
    <p style="color:white; text-align:justify;">
    The comparative analysis between rape cases and kidnapping/abduction for marriage (IPC 366) 
    highlights a consistent positive relationship across states. 
    The scatter plot clearly shows that regions with higher rape cases also tend to report 
    more kidnapping crimes. The horizontal bar chart provides an easy side-by-side comparison 
    for major states such as Rajasthan, Uttar Pradesh, and Bihar, which exhibit particularly 
    high levels of both crimes. The pie chart emphasizes that although rape cases remain the 
    majority, kidnapping offenses account for a significant share of total gender-related crimes. 
    These visuals collectively demonstrate the interconnected nature of gender-based offenses 
    and underline the urgent need for comprehensive awareness, legal protection, and enforcement efforts.
    </p>
    </div>
    """, unsafe_allow_html=True)

    # =============================
    # 💬 Interpretation / Discussion
    # =============================
    st.subheader("💬 Interpretation / Discussion")
    st.write("""
    The simplified visuals reveal a clear and strong connection between rape and kidnapping/abduction incidents.  
    **States with higher rape reports — such as Rajasthan, Uttar Pradesh, and Bihar — also show high kidnapping levels**, 
    suggesting similar social and cultural risk factors.  
    The grouped bar chart allows easy state-wise comparison, confirming that high population regions 
    contribute heavily to both crimes. The national pie chart clarifies that while rape cases dominate numerically, 
    kidnapping-for-marriage remains a persistent parallel issue.  
    This pattern implies that these crimes often coexist under shared conditions such as gender inequality, 
    weak deterrence, and inadequate awareness.  
    Thus, the findings highlight the importance of **integrated preventive strategies**, 
    combining education, legal reform, and stronger community engagement to reduce these intertwined crimes.
    """)
