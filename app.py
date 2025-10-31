import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------------
# PAGE CONFIGURATION
# ---------------------
st.set_page_config(page_title="Rape Statistics in India", layout="wide")

# ---------------------
# LOAD DATA
# ---------------------
@st.cache_data
def load_data():
    df = pd.read_csv("Rape cases dataset.csv")
    df.columns = df.columns.str.strip()  # Clean column names
    return df

df = load_data()

# ---------------------
# SIDEBAR NAVIGATION
# ---------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dataset Overview", "Objective 1", "Objective 2", "Objective 3"])

# ---------------------
# PAGE 1 - DATASET OVERVIEW
# ---------------------
if page == "Dataset Overview":
    st.title("📊 Dataset Overview")
    st.write("This dataset contains information on rape cases reported across Indian States and Union Territories in 2019. It includes details such as total cases, age-wise distribution, and related crimes.")
    
    st.dataframe(df.head())
    st.write(f"**Total Records:** {df.shape[0]} | **Columns:** {df.shape[1]}")

# ---------------------
# PAGE 2 - OBJECTIVE 1
# ---------------------
elif page == "Objective 1":
    st.title("Objective 1: Distribution of Rape Cases Across States (2019)")

    st.write("### 1️⃣ Bar Chart: Top 10 States by Total Rape Cases")
    top_states = df.sort_values(by="Total_rape cases registered_2019", ascending=False).head(10)
    fig = px.bar(top_states, x="State_UT", y="Total_rape cases registered_2019",
                 color="Total_rape cases registered_2019", title="Top 10 States by Total Rape Cases")
    st.plotly_chart(fig, use_container_width=True)

    st.write("### 2️⃣ Pie Chart: Adult vs Minor Victims (Overall)")
    adult = df["Adult_18_yrs_and_above"].sum()
    minor = df["Minor_below_18_yrs"].sum()
    fig2 = px.pie(values=[adult, minor], names=["Adult", "Minor"],
                  title="Proportion of Adult vs Minor Victims (2019)")
    st.plotly_chart(fig2, use_container_width=True)

    st.write("### 3️⃣ Scatter Plot: Total Cases vs Rape Rate")
    fig3 = px.scatter(df, x="Total_rape cases registered_2019", 
                      y="_2019_Rape_rate_percent_per_100000_pop",
                      text="State_UT", color="_2019_Rape_rate_percent_per_100000_pop",
                      title="Total Cases vs Rape Rate by State (2019)")
    st.plotly_chart(fig3, use_container_width=True)

# ---------------------
# PAGE 3 - OBJECTIVE 2
# ---------------------
elif page == "Objective 2":
    st.title("Objective 2: Trend and Change in Rape Rates (2018–2019)")

    st.write("### 1️⃣ Line Chart: Annual Change in Rape Rate by State")
    fig4 = px.line(df, x="State_UT", y="Annual_change_in_Rape_rate_2018_19",
                   title="Annual Change in Rape Rate (2018–2019)")
    st.plotly_chart(fig4, use_container_width=True)

    st.write("### 2️⃣ Scatter Plot: Change in Absolute Number vs Rate Change")
    fig5 = px.scatter(df, 
                      x="Annual_change_in_absolute_no_of_rape_cases_registered_2018_19", 
                      y="Annual_change_in_Rape_rate_2018_19",
                      text="State_UT", color="Annual_change_in_Rape_rate_2018_19",
                      title="Change in Cases vs Change in Rape Rate (2018–2019)")
    st.plotly_chart(fig5, use_container_width=True)

    st.write("### 3️⃣ Heatmap: Comparing Rape Rate and Annual Change")
    fig6, ax = plt.subplots()
    sns.heatmap(df[["_2019_Rape_rate_percent_per_100000_pop", "Annual_change_in_Rape_rate_2018_19"]].corr(), annot=True, cmap="coolwarm")
    st.pyplot(fig6)

# ---------------------
# PAGE 4 - OBJECTIVE 3
# ---------------------
elif page == "Objective 3":
    st.title("Objective 3: Correlation Between Rape Cases and Related Crimes")

    st.write("### 1️⃣ Scatter Plot: Rape vs Kidnapping (Section 366 IPC)")
    fig7 = px.scatter(df, x="Total_rape cases registered_2019",
                      y="Kidnapping_&_Abduction_of_Women_to_compel_her_for_marriage_Section_366_IPC",
                      text="State_UT", color="Total_rape cases registered_2019",
                      title="Rape Cases vs Kidnapping for Marriage (Section 366 IPC)")
    st.plotly_chart(fig7, use_container_width=True)

    st.write("### 2️⃣ Scatter Plot: Rape vs Procuration of Minor Girls (Section 366A)")
    fig8 = px.scatter(df, x="Total_rape cases registered_2019",
                      y="Procuration of Minor Girls (Section 366A IPC)",
                      text="State_UT", color="Total_rape cases registered_2019",
                      title="Rape Cases vs Procuration of Minor Girls (Section 366A IPC)")
    st.plotly_chart(fig8, use_container_width=True)

    st.write("### 3️⃣ Correlation Heatmap of All Crime Variables")
    fig9, ax = plt.subplots(figsize=(10, 5))
    sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap="coolwarm")
    st.pyplot(fig9)
