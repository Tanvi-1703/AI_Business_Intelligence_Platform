import pandas as pd

def export_excel(df):
    output_path = "reports/Sales_Report.xlsx"

    df.to_excel(output_path, index=False)

    return output_path