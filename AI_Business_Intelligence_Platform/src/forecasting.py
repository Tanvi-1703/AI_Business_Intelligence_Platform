from sklearn.linear_model import LinearRegression
import pandas as pd

def sales_forecast(df):
    temp = df.copy()

    temp["Month_Number"] = range(1, len(temp) + 1)

    X = temp[["Month_Number"]]
    y = temp["Sales"]

    model = LinearRegression()
    model.fit(X, y)

    next_month = [[len(temp) + 1]]

    prediction = model.predict(next_month)

    return round(prediction[0], 2)