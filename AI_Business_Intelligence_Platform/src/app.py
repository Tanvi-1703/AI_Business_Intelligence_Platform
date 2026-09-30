import streamlit as st
import pandas as pd

from data_cleaner import clean_dataset
from analytics_engine import dashboard, top_sales
from visualization import sales_by_region


st.set_page_config(
    page_title="AI Business Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI BUSINESS INTELLIGENCE PLATFORM")
st.subheader("Business Intelligence Dashboard")

st.write(
    "Upload your sales dataset to clean, analyze and visualize your business data."
)

uploaded_file = st.file_uploader(
    "Upload CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("Dataset uploaded successfully!")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Clean data
    df = clean_dataset(df)

    st.subheader("Cleaned Dataset")
    st.dataframe(df.head())

    # KPIs
    st.subheader("📈 Business KPIs")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Sales", f"₹{df['sales'].sum():,.2f}")

    if "profit" in df.columns:
        col2.metric("Total Profit", f"₹{df['profit'].sum():,.2f}")

    if "orders" in df.columns:
        col3.metric("Total Orders", f"{df['orders'].sum():,.0f}")

    col4.metric("Rows", f"{len(df):,}")

    # Sales by region
    if "region" in df.columns and "sales" in df.columns:

        st.subheader("🌍 Sales by Region")

        region_sales = df.groupby("region")["sales"].sum()

        st.bar_chart(region_sales)

    # Monthly sales
    if "month" in df.columns and "sales" in df.columns:

        st.subheader("📅 Monthly Sales")

        monthly = df.groupby("month")["sales"].sum()

        st.line_chart(monthly)

    st.subheader("🔝 Top Sales")

    if "sales" in df.columns:
        st.dataframe(
            df.sort_values("sales", ascending=False).head(5)
        )

else:

    st.info("👆 Please upload a CSV file to get started.")
