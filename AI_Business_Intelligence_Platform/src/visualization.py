import os
import matplotlib.pyplot as plt
import plotly.express as px


IMAGE_FOLDER = "reports/images"

os.makedirs(IMAGE_FOLDER, exist_ok=True)


def sales_by_region(df):

    region = df.groupby("region")["sales"].sum()

    plt.figure(figsize=(8,5))

    plt.bar(region.index, region.values)

    plt.title("Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Sales")

    plt.tight_layout()

    plt.savefig(f"{IMAGE_FOLDER}/sales_by_region.png")

    plt.show()

    plt.close()


def monthly_sales(df):

    month = df.groupby("month")["sales"].sum()

    plt.figure(figsize=(9,5))

    plt.plot(
        month.index,
        month.values,
        marker="o"
    )

    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Sales")

    plt.tight_layout()

    plt.savefig(f"{IMAGE_FOLDER}/monthly_sales.png")

    plt.show()

    plt.close()


def profit_distribution(df):

    profit = df.groupby("region")["profit"].sum()

    plt.figure(figsize=(6,6))

    plt.pie(
        profit.values,
        labels=profit.index,
        autopct="%1.1f%%"
    )

    plt.title("Profit Distribution")

    plt.savefig(f"{IMAGE_FOLDER}/profit_distribution.png")

    plt.show()

    plt.close()


def interactive_sales(df):

    fig = px.bar(
        df,
        x="region",
        y="sales",
        color="region",
        title="Interactive Sales by Region"
    )

    fig.show()