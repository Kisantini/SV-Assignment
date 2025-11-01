import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def show():
    st.title("Objective 2: Annual Change and Trend Analysis (2018–2019)")
    st.write("""
    **Goal:** To examine the yearly change in rape rates and case numbers across Indian states 
    between 2018 and 2019, highlighting states that experienced significant improvement or deterioration.
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
    st.caption("🔍 *A positive value means the rape rate increased compared to 2018, while negative values indicate improvement.*")

    # =============================
    # 2️⃣ Bar Chart – Comparison of Total Cases vs Rate Change
    # =============================
    st.subheader("2️⃣ Comparison of Total Cases and Rate Change (2019)")
    fig2 = px.bar(
        df.sort_values(by="Annual Change in Rape Rate (2018-19)", ascending=False),
        x="State/UT",
        y=["Total Rape Cases 2019", "Annual Change in Rape Rate (2018-19)"],
        barmode="group",
        title="Comparison: Total Rape Cases vs Annual Rate Change (2018–2019)",
        labels={"value": "Values", "variable": "Metric"}
    )
    st.plotly_chart(fig2, use_container_width=True)
    st.caption("🔍 *The grouped bars show how states with higher case counts also tend to experience larger changes in rate.*")

    # =============================
    # 3️⃣ Area Chart – Trend of Rate Change Across States
    # =============================
    st.subheader("3️⃣ Distribution of Rate Changes Across States")
    sorted_rate = df.sort_values(by="Annual Change in Rape Rate (2018-19)")
    fig3 = px.area(
        sorted_rate,
        x="State/UT",
        y="Annual Change in Rape Rate (2018-19)",
        color_discrete_sequence=["#ff7f50"],
        title="Positive and Negative Rape Rate Changes (2018–2019)"
    )
    fig3.update_layout(xaxis_title="State / UT", yaxis_title="Rate Change (per 100,000 population)")
    st.plotly_chart(fig3, use_container_width=True)
    st.caption("🔍 *The area chart visually separates states with positive and negative changes, highlighting overall patterns.*")

    # =============================
    # 🧾 Summary Box (Black Background)
    # =============================
    st.subheader("📦 Summary Box")
    st.markdown("""
    <div style="background-color:#1e1e1e; padding:15px; border-radius:10px;">
    <p style="color:white; text-align:justify;">
    The comparative analysis between 2018 and 2019 reveals that rape rate changes vary significantly across Indian states. 
    States such as Rajasthan and Assam experienced a clear rise in rape rates, while regions like Gujarat and Andhra Pradesh 
    recorded modest decreases. The bar visualization confirms that areas with a larger number of cases also tend to exhibit 
    more substantial changes in their rate per population, suggesting a close link between total case volume and rate variation. 
    The area chart shows that most states lie close to the neutral line, indicating minor fluctuations, while a few outliers 
    stand out with noticeable increases. Overall, this trend reflects the need for more consistent reporting systems 
    and focused preventive measures in high-variation states.
    </p>
    </div>
    """, unsafe_allow_html=True)

    # =============================
    # 💬 Interpretation / Discussion
    # =============================
    st.subheader("💬 Interpretation / Discussion")
    st.write("""
    The visualizations demonstrate that while most states maintained relatively stable rape rates between 2018 and 2019, 
    a handful of regions displayed substantial changes. States like **Rajasthan, Assam, and Madhya Pradesh** 
    show significant increases in rate and total case numbers, which could stem from higher reporting awareness 
    or actual growth in incidents. Conversely, states with slight declines indicate improvements in either reporting 
    control or prevention efforts.  
    The grouped bar chart visually supports the hypothesis that **higher case volumes tend to correspond with 
    greater rate volatility**, indicating population-normalized growth.  
    The area chart makes the national trend clearer—most states fluctuate around zero, meaning the overall change 
    was relatively small nationwide.  
    This finding highlights the importance of **sustained data-driven monitoring and localized intervention programs**.
    """)
