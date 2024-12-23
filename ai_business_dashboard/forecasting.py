from prophet import Prophet

def forecast_with_prophet(df, column, periods):
    prophet_df = df[['Date', column]].rename(columns={'Date': 'ds', column: 'y'})
    model = Prophet()
    model.fit(prophet_df)

    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)

    return forecast[['ds', 'yhat']].rename(columns={'ds': 'Date', 'yhat': column})
