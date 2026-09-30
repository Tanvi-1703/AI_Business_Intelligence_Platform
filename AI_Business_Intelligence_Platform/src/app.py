import streamlit as st
import pandas as pd
import plotly.express as px

from forecasting import sales_forecast
from excel_export import export_excel
from pdf_report import export_pdf

st.set_page_config(
    page_title="AI Business Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Business Intelligence Dashboard")

# Load cleaned data
uploaded_file = st.sidebar.file_uploader(
    "Upload Sales CSV",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv(
        "AI_Business_Intelligence_Platform/data/cleaned/cleaned_sales.csv"
    )

# Convert column names to Title Case
df.columns = df.columns.str.strip().str.title()

# ---------------- Sidebar ----------------

st.sidebar.header("Filters")

regions = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

months = st.sidebar.multiselect(
    "Select Month",
    options=df["Month"].unique(),
    default=df["Month"].unique()
)

filtered_df = df[
    (df["Region"].isin(regions)) &
    (df["Month"].isin(months))
]

# ---------------- KPI Cards ----------------

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Orders"].sum()
average_sales = filtered_df["Sales"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Total Sales", f"{total_sales:,}")
col2.metric("📈 Total Profit", f"{total_profit:,}")
col3.metric("🛒 Orders", f"{total_orders:,}")
col4.metric("📊 Avg Sales", f"{average_sales:,.2f}")

st.divider()

# ---------------- Sales by Region ----------------

fig = px.bar(
    filtered_df,
    x="Region",
    y="Sales",
    color="Region",
    title="Sales by Region"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------- Profit by Region ----------------

fig2 = px.pie(
    filtered_df,
    values="Profit",
    names="Region",
    title="Profit Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------- Monthly Sales ----------------

fig3 = px.line(
    filtered_df,
    x="Month",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------- Data Table ----------------

st.subheader("Dataset")
st.dataframe(filtered_df)

# ---------------- Forecast ----------------

prediction = sales_forecast(filtered_df)

st.subheader("📈 AI Sales Forecast")

st.success(
    f"Expected Next Month Sales: ₹{prediction:,.2f}"
)

st.divider()

# ---------------- Export Report ----------------

st.subheader("📥 Export Report")

excel_file = export_excel(filtered_df)

with open(excel_file, "rb") as file:
    st.download_button(
        label="📊 Download Excel Report",
        data=file,
        file_name="Sales_Report.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

pdf_file = export_pdf(filtered_df)

with open(pdf_file, "rb") as file:
    st.download_button(
        label="📄 Download PDF Report",
        data=file,
        file_name="Sales_Report.pdf",
        mime="application/pdf"
    )
