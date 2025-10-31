import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------------
# PAGE CONFIGURATION
# ---------------------
st.set_page_config(page_title="Rape Cases in India (2019)", layout="wide")

# ---------------------
# LOAD DATA
# ---------------------
@st.cache_data
def load_data():
    df = pd.read_csv("Rape cases dataset.csv")
    df.columns = df.columns.str.strip()  # remove extra spaces
    return df

df = load_data()

# ---------------------
# SIDEBAR NAVIGATION
# ---------------------
st.sidebar.title("📑 Navigation")
page = st.sidebar.radio("Go to", ["Dataset Overview", "Objective 1", "Objective 2", "Objective 3"])

# ---------------------
# PAGE 1: DATASET OVERVIEW
# ---------------------
if page == "Dataset Overview":
    st.title("📊 Dataset Overview – Rape Cases in India (2019)")
    st.write("""
    This dataset provides details of rape cases across Indian States and Union Territories in 2019. 
    It includes total cases, adult/minor distribution, rate per 100k population, and related crimes 
    such as kidnapping/abduction for marriage (IPC 366). 
    """)

    st.dataframe(df)
    st.write(f"**Total Records:** {df.shape[0]} | **Columns:** {df.shape[1]}")

    st.write("### Column Descriptions")
    st.markdown("""
    - **State/UT:** State or Union Territory name  
    - **Total Rape Cases 2019:** Total cases reported in 2019  
    - **Adult Cases (18+ yrs):** Number of adult victims  
    - **Minor Cases (<18 yrs):** Number of minor victims  
    - **2019 Rape Rate (per 100k pop):** Rate per 100,000 population  
    - **Annual Change in Rape Rate (2018–19):** Year-over-year rate change  
    - **Annual Change in Cases (2018–19):** Change in number of cases from 2018  
    - **Kidnapping/Abduction for Marriage (IPC 366):** Related crime statistic
    """)

# ---------------------
# PAGE 2: OBJECTIVE 1
# ---------------------
elif page == "Objective 1":
    st.title("Objective 1: Distribution of Rape Cases Across States (2019)")

    st.write("""
    **Goal:** To understand how rape cases are distributed across different states and age groups in India.
    """)

    # Bar Chart - Top 10 States by Total Rape Cases
    st.subheader("1️⃣ Top 10 States by Total Rape Cases")
    top_states = df.sort_values(by="Total Rape Cases 2019", ascending=False).head(10)
    fig1 = px.bar(top_states, x="State/UT", y="Total Rape Cases 2019",
                  color="Total Rape Cases 2019", title="Top 10 States by Total Rape Cases (2019)")
    st.plotly_chart(fig1, use_container_width=True)

    # Pie Chart - Adult vs Minor Victims (India total)
    st.subheader("2️⃣ Overall Proportion of Adult vs Minor Victims")
    adult = df["Adult Cases (18+ yrs)"].sum()
    minor = df["Minor Cases (<18 yrs)"].sum()
    fig2 = px.pie(values=[adult, minor], names=["Adult Victims (18+)", "Minor Victims (<18)"],
                  title="Adult vs Minor Victims (India, 2019)")
    st.plotly_chart(fig2, use_container_width=True)

    # Scatter Plot - Total Cases vs Rape Rate
    st.subheader("3️⃣ Rape Rate vs Total Cases by State")
    fig3 = px.scatter(df, x="Total Rape Cases 2019", 
                      y="2019 Rape Rate (per 100k pop)",
                      text="State/UT", color="2019 Rape Rate (per 100k pop)",
                      title="Rape Rate vs Total Cases (2019)")
    st.plotly_chart(fig3, use_container_width=True)

# ---------------------
# PAGE 3: OBJECTIVE 2
# ---------------------
elif page == "Objective 2":
    st.title("Objective 2: Change in Rape Rates and Cases (2018–2019)")

    st.write("""
    **Goal:** To analyze the annual change in rape rate and total cases across Indian states between 2018 and 2019.
    """)

    # Line Chart - Annual Change in Rape Rate by State
    st.subheader("1️⃣ Annual Change in Rape Rate (2018–2019)")
    fig4 = px.bar(df, x="State/UT", y="Annual Change in Rape Rate (2018-19)",
                  title="Annual Change in Rape Rate by State (2018–2019)",
                  color="Annual Change in Rape Rate (2018-19)")
    st.plotly_chart(fig4, use_container_width=True)

    # Scatter Plot - Rate Change vs Absolute Case Change
    st.subheader("2️⃣ Change in Cases vs Change in Rape Rate")
    fig5 = px.scatter(df,
                      x="Annual Change in Cases (2018-19)",
                      y="Annual Change in Rape Rate (2018-19)",
                      text="State/UT", color="Annual Change in Rape Rate (2018-19)",
                      title="Change in Cases vs Rape Rate (2018–2019)")
    st.plotly_chart(fig5, use_container_width=True)

    # Heatmap - Correlation of Key Variables
    st.subheader("3️⃣ Correlation Between Rape Rate and Annual Change")
    fig6, ax = plt.subplots()
    sns.heatmap(df[["2019 Rape Rate (per 100k pop)", "Annual Change in Rape Rate (2018-19)", "Annual Change in Cases (2018-19)"]].corr(), 
                annot=True, cmap="coolwarm", fmt=".2f")
    st.pyplot(fig6)

# ---------------------
# PAGE 4: OBJECTIVE 3
# ---------------------
elif page == "Objective 3":
    st.title("Objective 3: Relationship Between Rape Cases and Related Crimes")

    st.write("""
    **Goal:** To explore correlations between rape cases and related crimes such as 
    kidnapping or abduction for marriage under Section 366 IPC.
    """)

    # Scatter Plot - Rape vs Kidnapping for Marriage
    st.subheader("1️⃣ Rape Cases vs Kidnapping for Marriage (IPC 366)")
    fig7 = px.scatter(df, x="Total Rape Cases 2019",
                      y="Kidnapping/Abduction for Marriage (IPC 366)",
                      text="State/UT", color="Total Rape Cases 2019",
                      title="Rape Cases vs Kidnapping for Marriage (IPC 366)")
    st.plotly_chart(fig7, use_container_width=True)

    # Correlation Heatmap
    st.subheader("2️⃣ Correlation Heatmap of Crime Indicators")
    numeric_df = df.select_dtypes(include='number')
    fig8, ax = plt.subplots(figsize=(10, 5))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    st.pyplot(fig8)

    # Summary Insight
    st.subheader("3️⃣ Observation Summary")
    st.info("""
    - States with higher total rape cases often show elevated values in related crimes.
    - Positive correlation suggests overlapping socio-legal factors.
    - Deeper policy analysis can reveal regional drivers for both rape and abduction crimes.
    """)
