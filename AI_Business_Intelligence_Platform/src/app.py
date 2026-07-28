from utils import print_title

from data_loader import load_dataset
from data_loader import dataset_summary

from data_cleaner import clean_dataset
from data_cleaner import save_clean_dataset

from analytics_engine import dashboard
from analytics_engine import top_sales

from visualization import sales_by_region
from visualization import monthly_sales
from visualization import profit_distribution
from visualization import interactive_sales

from sql_manager import save_to_database
from sql_manager import read_database

def start():

    print_title("AI BUSINESS INTELLIGENCE PLATFORM")

    # Load Dataset
    df = load_dataset("sales.csv")

    if df is None:
        return

    # Dataset Summary
    dataset_summary(df)

    # Clean Dataset
    df = clean_dataset(df)

    # Save Clean CSV
    save_clean_dataset(df)

    # Save SQL
    save_to_database(df)

    # Read SQL
    sql_df = read_database()

    print("\n========== BUSINESS KPIs ==========\n")

    summary = dashboard(sql_df)

    for key, value in summary.items():
        print(f"{key:<25}: {value}")

    print("\n========== TOP 5 SALES ==========\n")

    print(top_sales(sql_df))
    
    print("\nGenerating Charts...\n")

    sales_by_region(sql_df)

    monthly_sales(sql_df)

    profit_distribution(sql_df)

    interactive_sales(sql_df)

    print("\nCharts Generated Successfully.")