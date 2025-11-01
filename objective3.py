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
    # 2️⃣ Box Plot – Distribution of Kidnapping/Abduction Cases Across States
    # =============================
    st.subheader("2️⃣ Distribution of Kidnapping/Abduction for Marriage Cases (IPC 366)")
    fig2 = px.box(
        df,
        y="Kidnapping/Abduction for Marriage (IPC 366)",
        points="all",
        title="Spread of Kidnapping/Abduction for Marriage Cases Across States (2019)",
        color_discrete_sequence=["#ff7f50"]
    )
    fig2.update_layout(yaxis_title="Number of Kidnapping/Abduction Cases")
    st.plotly_chart(fig2, use_container_width=True)
    st.caption("🔍 *The box plot shows that a few states have extremely high kidnapping counts, while most remain near the lower range.*")

    # =============================
    # 3️⃣ Correlation Heatmap – Relationship Among Key Indicators
    # =============================
    st.subheader("3️⃣ Correlation Heatmap of Crime Indicators")
    selected_cols = [
        "Total Rape Cases 2019",
        "2019 Rape Rate (per 100k pop)",
        "Annual Change in Rape Rate (2018-19)",
        "Kidnapping/Abduction for Marriage (IPC 366)"
    ]
    fig3, ax = plt.subplots(figsize=(7, 4))
    sns.heatmap(df[selected_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
    ax.set_title("Correlation Among Rape and Related Crime Variables")
    st.pyplot(fig3)
    st.caption("🔍 *High positive correlation values indicate that regions with more rape cases also experience more kidnapping incidents.*")

    # =============================
    # 🧾 Summary Box (Black Background)
    # =============================
    st.subheader("📦 Summary Box")
    st.markdown("""
    <div style="background-color:#1e1e1e; padding:15px; border-radius:10px;">
    <p style="color:white; text-align:justify;">
    This analysis reveals a close association between rape cases and related crimes like 
    kidnapping or abduction for marriage (IPC 366). The scatter plot highlights a strong 
    positive relationship, where states reporting more rape cases also record higher kidnapping incidents. 
    The box plot shows significant variation, with a few states emerging as outliers with extremely 
    high kidnapping numbers, while most states fall within a moderate range. 
    The correlation heatmap confirms that these crimes are positively correlated, 
    suggesting shared underlying causes such as gender inequality, social pressure, 
    and inadequate legal deterrence. These findings emphasize the importance of coordinated 
    preventive measures and improved enforcement mechanisms across regions.
    </p>
    </div>
    """, unsafe_allow_html=True)

    # =============================
    # 💬 Interpretation / Discussion
    # =============================
    st.subheader("💬 Interpretation / Discussion")
    st.write("""
    The updated visuals provide a clearer picture of how related crimes interact across regions.  
    The scatter plot shows a **strong positive correlation** between rape and kidnapping-for-marriage cases, 
    implying shared social roots and behavioral patterns.  
    The **box plot** highlights that most states report relatively low kidnapping rates, 
    but a few (like **Rajasthan, Uttar Pradesh, and Bihar**) act as statistical outliers — 
    representing much higher incident counts than the national average.  
    These outliers suggest deep-rooted cultural and socio-economic factors influencing both crimes.  
    The heatmap strengthens this observation, confirming a **consistent positive relationship** 
    among crime categories.  
    Overall, the analysis underlines the need for **comprehensive social reform, education programs, 
    and better coordination between law enforcement agencies** to mitigate such interconnected offenses.
    """)
