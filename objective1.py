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
ax.set_xlabel("Rape Rate per 100,000 Population")   # ✅ Fixed: label text provided
ax.set_ylabel("Number of States/UTs")
ax.set_title("Distribution of Rape Rate Across States (2019)")

st.pyplot(fig3)
st.caption("🔍 *Most states fall in the lower rape rate range (1–6 per 100,000 population), with a few outliers having significantly higher rates.*")
