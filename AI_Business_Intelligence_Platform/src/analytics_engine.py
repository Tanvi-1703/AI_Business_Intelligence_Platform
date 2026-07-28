import pandas as pd


def total_sales(df):
    return df["sales"].sum()


def total_profit(df):
    return df["profit"].sum()


def total_orders(df):
    return df["orders"].sum()


def average_sales(df):
    return round(df["sales"].mean(), 2)


def best_region(df):
    return (
        df.groupby("region")["sales"]
        .sum()
        .idxmax()
    )


def best_month(df):
    return (
        df.groupby("month")["sales"]
        .sum()
        .idxmax()
    )


def highest_profit_region(df):
    return (
        df.groupby("region")["profit"]
        .sum()
        .idxmax()
    )


def highest_orders_region(df):
    return (
        df.groupby("region")["orders"]
        .sum()
        .idxmax()
    )


def top_sales(df):
    return df.sort_values(
        by="sales",
        ascending=False
    ).head(5)


def dashboard(df):

    return {
        "Total Sales": total_sales(df),
        "Total Profit": total_profit(df),
        "Total Orders": total_orders(df),
        "Average Sales": average_sales(df),
        "Best Region": best_region(df),
        "Best Month": best_month(df),
        "Highest Profit Region": highest_profit_region(df),
        "Highest Orders Region": highest_orders_region(df)
    }