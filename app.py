import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page setup
st.set_page_config(page_title="Telecom Churn Dashboard", layout="wide")
st.title("📞 Telecom Customer Churn Analysis")

# Load data
df = pd.read_csv("Customer Churn.csv")

# Sidebar filters
st.sidebar.header("📊 Filter the Data")

gender_filter = st.sidebar.multiselect("Select Gender", options=df["gender"].unique(), default=df["gender"].unique())
churn_filter = st.sidebar.multiselect("Select Churn Status", options=df["Churn"].unique(), default=df["Churn"].unique())
contract_filter = st.sidebar.multiselect("Select Contract Type", options=df["Contract"].unique(), default=df["Contract"].unique())
internet_filter = st.sidebar.multiselect("Select Internet Service", options=df["InternetService"].unique(), default=df["InternetService"].unique())
# senior_filter = st.sidebar.multiselect("Select Senior Citizen", options=[0, 1], default=[0, 1])
senior_label_map = {0: "No", 1: "Yes"}
reverse_senior_map = {"No": 0, "Yes": 1}

senior_filter_labels = st.sidebar.multiselect(
    "Select Senior Citizen",
    options=["No", "Yes"],
    default=["No", "Yes"]
)
senior_filter = [reverse_senior_map[label] for label in senior_filter_labels]
payment_filter = st.sidebar.multiselect("Select Payment Method", options=df["PaymentMethod"].unique(), default=df["PaymentMethod"].unique())

tenure_min = int(df['tenure'].min())
tenure_max = int(df['tenure'].max())
tenure_range = st.sidebar.slider("Select Tenure Range", min_value=tenure_min, max_value=tenure_max, value=(tenure_min, tenure_max))

charges_min = int(df['MonthlyCharges'].min())
charges_max = int(df['MonthlyCharges'].max())
charges_range = st.sidebar.slider("Select Monthly Charges Range", min_value=charges_min, max_value=charges_max, value=(charges_min, charges_max))

# Apply filters
filtered_df = df[
    (df["gender"].isin(gender_filter)) &
    (df["Churn"].isin(churn_filter)) &
    (df["Contract"].isin(contract_filter)) &
    (df["InternetService"].isin(internet_filter)) &
    (df["SeniorCitizen"].isin(senior_filter)) &
    (df["PaymentMethod"].isin(payment_filter)) &
    (df["tenure"].between(tenure_range[0], tenure_range[1])) &
    (df["MonthlyCharges"].between(charges_range[0], charges_range[1]))
]

# Show data preview
st.subheader("🔍 Dataset Preview")
# st.dataframe(filtered_df.head())

# Show full filtered dataset (expandable)
with st.expander(" Click to view the full filtered dataset"):
    st.dataframe(filtered_df)

# Download button for full filtered dataset
csv = filtered_df.to_csv(index=False).encode('utf-8')
# st.download_button(
#     label="📥 Download Filtered Dataset as CSV",
#     data=csv,
#     file_name='filtered_telecom_churn_data.csv',
#     mime='text/csv'
# )


# Utility functions
def show_centered_plot(fig, width=6):
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.pyplot(fig)

def show_insight(text):
    st.markdown(f"<div style='font-size:18px; color:#333; background-color:#f1f1f1; padding:10px; border-radius:8px'><b>Insight:</b> {text}</div>", unsafe_allow_html=True)

# ----------------------
# Churn by Gender
st.subheader("📊 Churn by Gender")
fig, ax = plt.subplots(figsize=(6, 4))
sns.countplot(x='gender', data=filtered_df, hue='Churn', ax=ax)
ax.set_title("Churn by Gender")
show_centered_plot(fig)
show_insight("Churn is slightly higher among female customers compared to male customers.")

# ----------------------
# Churn by Senior Citizen
st.subheader("🧓 Churn by Senior Citizen (Stacked Bar)")
filtered_df['SeniorCitizenLabel'] = filtered_df['SeniorCitizen'].map({0: 'No', 1: 'Yes'})
total_counts = filtered_df.groupby('SeniorCitizenLabel')['Churn'].value_counts(normalize=True).unstack() * 100
fig2, ax2 = plt.subplots(figsize=(5, 4))
total_counts.plot(kind='bar', stacked=True, ax=ax2, color=['#1f77b4', '#ff7f0e'])
for p in ax2.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy()
    ax2.text(x + width / 2, y + height / 2, f'{height:.1f}%', ha='center', va='center')
plt.title('Churn by Senior Citizen')
plt.xlabel('Senior Citizen')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=0)
plt.legend(title='Churn')
show_centered_plot(fig2)
show_insight("Senior citizens have a noticeably higher churn rate.")

# ----------------------
# Tenure Distribution by Churn
st.subheader("📈 Tenure Distribution by Churn")
fig3, ax3 = plt.subplots(figsize=(8, 4))
sns.histplot(x='tenure', data=filtered_df, bins=72, hue='Churn', ax=ax3)
ax3.set_title("Tenure Distribution by Churn")
show_centered_plot(fig3)
show_insight("Most churn occurs in the early months of tenure, especially within the first 10 months.")

# ----------------------
# Churn by Contract Type
st.subheader("📋 Churn by Contract Type")
fig4, ax4 = plt.subplots(figsize=(6, 4))
sns.countplot(x='Contract', data=filtered_df, hue='Churn', ax=ax4)
ax4.set_title("Churn by Contract Type") 
show_centered_plot(fig4)
show_insight("Month-to-month contract users churn much more than others.")

# ----------------------
# Churn by Services Used
st.subheader("🛠️ Churn by Services Used")
columns = ['PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
           'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']
n_cols = 3
n_rows = (len(columns) + n_cols - 1) // n_cols
fig5, axes = plt.subplots(n_rows, n_cols, figsize=(14, n_rows * 3.5))
axes = axes.flatten()
for i, col in enumerate(columns):
    sns.countplot(x=col, data=filtered_df, ax=axes[i], hue=filtered_df["Churn"])
    axes[i].set_title(f'Churn by {col}')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Count')
for j in range(i + 1, len(axes)):
    fig5.delaxes(axes[j])
plt.tight_layout()
show_centered_plot(fig5)
show_insight("Customers without support services tend to churn more.")

# ----------------------
# Churn by Payment Method
st.subheader("💳 Churn by Payment Method")
fig6, ax6 = plt.subplots(figsize=(6, 4))

# ax = sns.countplot(x="PaymentMethod", data=filtered_df, hue="Churn")
# ax.bar_label(ax.containers[0])
# ax.bar_label(ax.containers[1])
ax = sns.countplot(x="PaymentMethod", data=filtered_df, hue="Churn")

# Safe bar labeling (works even if only one hue exists)
for container in ax.containers:
    ax.bar_label(container)

plt.title("Churn by Payment Method")
plt.xticks(rotation=45)

show_centered_plot(fig6)
show_insight("Electronic Check users churn more — potential trust or friction issues.")

# ----------------------
# Heatmap of Tenure vs Monthly Charges
st.subheader("🔥 Churn Heatmap (Tenure vs Monthly Charges)")
df_heatmap = filtered_df.copy()
df_heatmap['TenureGroup'] = pd.cut(df_heatmap['tenure'], bins=[0, 6, 12, 24, 48, 72], labels=["0-6", "6-12", "12-24", "24-48", "48-72"])
df_heatmap['ChargeGroup'] = pd.cut(df_heatmap['MonthlyCharges'], bins=[0, 30, 60, 90, 120], labels=["0-30", "30-60", "60-90", "90-120"])
pivot = pd.pivot_table(df_heatmap, values='customerID', index='TenureGroup',
                       columns='ChargeGroup', aggfunc=lambda x: df_heatmap.loc[x.index, 'Churn'].eq('Yes').mean(),
                       observed=False)
fig7, ax7 = plt.subplots(figsize=(8, 5))
sns.heatmap(pivot, annot=True, cmap="Reds", fmt=".2f", ax=ax7)
plt.title("Churn Rate Heatmap by Tenure and Monthly Charges")
plt.xlabel("Monthly Charges Group")
plt.ylabel("Tenure Group")
plt.tight_layout()
show_centered_plot(fig7)
show_insight("Churn is highest in the first 6 months for high-charge users (₹90–₹120).")

# ----------------------
# Insights block
st.markdown("<h2 style='margin-top:40px'>📌 Summary & Recommendations</h2>", unsafe_allow_html=True)

st.markdown("""
<div style='font-size:17px; line-height:1.6'>
<h4><b>🧠 Key Findings</b></h4>
<ul>
  <li><b>New, High-Paying Customers Churn the Most</b>: Especially those with <i>tenure &lt; 6 months</i> and <i>charges > ₹90</i>.</li>
  <li><b>Senior Citizens Are at Risk</b>: Need better onboarding, support, and possibly simpler plans.</li>
  <li><b>Long-Term Customers Stay</b>: Loyalty increases after 24 months even at high prices.</li>
  <li><b>Month-to-Month Users Are Volatile</b>: Much higher churn rate than contract users.</li>
  <li><b>Support Services Reduce Churn</b>: Tech Support, Security, and Backup features correlate with loyalty.</li>
  <li><b>Electronic Check Payment = Risk</b>: Needs investigation into user trust/friction.</li>
</ul>

<h4><b>✅ Recommendations</b></h4>
<ul>
  <li>Provide discounts, onboarding calls, or welcome benefits in the first 6 months.</li>
  <li>Incentivize upgrades to long-term contracts.</li>
  <li>Bundle security/support services as default in new user plans.</li>
  <li>Offer senior-friendly plans with simple UIs and billing.</li>
  <li>Investigate why Electronic Check users leave — streamline payment flow.</li>
</ul>

<h4><b>🎯 Focus Zones</b></h4>
<ul>
  <li>Senior Citizens</li>
  <li>Tenure &lt; 6 Months</li>
  <li>Monthly Charges &gt; ₹90</li>
  <li>Month-to-Month Contracts</li>
  <li>Electronic Check Payments</li>
</ul>
</div>
""", unsafe_allow_html=True)


from matplotlib.backends.backend_pdf import PdfPages
from io import BytesIO

# Create a button to download all plots as PDF
st.markdown("## 📥 Export Plots as PDF")

# Create a BytesIO buffer to hold the PDF in memory
pdf_buffer = BytesIO()

with PdfPages(pdf_buffer) as pdf:
    # Add all figures to the PDF
    pdf.savefig(fig)     # Churn by Gender
    pdf.savefig(fig2)    # Churn by Senior Citizen
    pdf.savefig(fig3)    # Tenure Distribution
    pdf.savefig(fig4)    # Churn by Contract Type
    pdf.savefig(fig5)    # Services Used (multiple subplots)
    pdf.savefig(fig6)    # Payment Method
    pdf.savefig(fig7)    # Heatmap

# Move to start of the buffer
pdf_buffer.seek(0)

# Streamlit download button
st.download_button(
    label="Download All Plots as PDF",
    data=pdf_buffer,
    file_name="telecom_churn_analysis.pdf",
    mime="application/pdf"
)



