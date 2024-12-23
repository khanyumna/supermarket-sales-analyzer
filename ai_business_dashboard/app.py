from data_processing import load_and_prepare_data
from modeling import train_and_evaluate
from forecasting import forecast_with_prophet
from dash_app import create_dash_app
import pandas as pd


# File paths
DATA_PATH = r"C:\Users\yumna\OneDrive\CS Learning\ai_business_dashboard\data\supermarket_sales new.csv"
DB_PATH = r"C:\Users\yumna\OneDrive\CS Learning\ai_business_dashboard\data\business_dashboard.db"


# Load and process data
df = load_and_prepare_data(DATA_PATH, DB_PATH)

# Prepare features and targets
X = df[['Days', 'Costs', 'Costs_Rolling_Avg', 'Revenue_Rolling_Avg', 'Profit_Margins', 'Units_Sold_Rolling_Avg']]
y_revenue = df['Revenue']
y_profit_margins = df['Profit_Margins']
y_units_sold = df['Quantity']

# Train models
print("\nEvaluating Revenue Model:")
model_revenue, _ = train_and_evaluate(X, y_revenue)

print("\nEvaluating Profit Margins Model:")
model_profit_margins, _ = train_and_evaluate(X, y_profit_margins)

print("\nEvaluating Units Sold Model:")
model_units_sold, _ = train_and_evaluate(X, y_units_sold)

# Forecast future data
print("\nGenerating Future Forecasts:")
revenue_forecast = forecast_with_prophet(df, 'Revenue', 7)
profit_margin_forecast = forecast_with_prophet(df, 'Profit_Margins', 7)
units_sold_forecast = forecast_with_prophet(df, 'Quantity', 7)

# Combine actual and forecasted data
forecast_df = revenue_forecast.merge(profit_margin_forecast, on='Date').merge(units_sold_forecast, on='Date')
combined_df = pd.concat([
    df[['Date', 'Revenue', 'Profit_Margins', 'Quantity']].rename(
        columns={
            'Revenue': 'Revenue (Actual)',
            'Profit_Margins': 'Profit Margins (Actual)',
            'Quantity': 'Units Sold (Actual)'
        }
    ),
    forecast_df.rename(
        columns={
            'Revenue': 'Revenue (Forecast)',
            'Profit_Margins': 'Profit Margins (Forecast)',
            'Quantity': 'Units Sold (Forecast)'
        }
    )
])

# Create and run the Dash app
app = create_dash_app(combined_df)

if __name__ == "__main__":
    app.run_server(debug=False)
