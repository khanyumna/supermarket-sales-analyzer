# Supermarket Sales Analyzer 📈

## Description
This project is a dashboard application that analyzes supermarket sales data, predicts trends and visualizes key metrics such as revenue, profit margins, and units sold.

## Features
- Revenue trends, profit margin trends, units sold trends
- Predictions for each using Prophet

## How to Run
1. Clone the repository
2. Set up virtual environment:
   - "python -m venv venv"
   -  source venv\Scripts\activate (on windows)
   -  source venv/bin/activate (on Mac)
3. Install dependences
    - pip install -r requirments.txt
4. Run the app
    - python app.py

## Dataset
Dataset used: [Market Sales Data on Kaggle](https://www.kaggle.com/datasets/willianoliveiragibin/market-sales-data?resource=download)

## Technologies Used
- Python
- SQLite for processed data
- scikit-learn for machine learning/model training and evaluation
- Prophet for time-series forecasting
- Dash for building the web app
- Plotly for creating the graphs

## Output for Model Performance

Revenue:
R^2: 1.00, RMSE: 14.06, MAE: 3.06

Profit Margins:
R^2: 1.00, RMSE: 0.00, MAE: 0.00

Units Sold:
R^2: 0.68, RMSE: 1.71, MAE: 1.35

## Challenges
- Static Dataset: the dataset lacked real-time updates, limiting the model's ability to generalize future trends. A dynamic data source would improve usability.
- Overfitting: Models achieved perfect R^2 scores for revenue and profit margins, likely due to overfitting.
- Applicablity of ML: Predictions were restricted by static data (Model was memorizing instead of learning).

## Screenshots
![image](https://github.com/user-attachments/assets/eac8d14f-6937-4d45-98bb-13c3e1b568c4)
![image](https://github.com/user-attachments/assets/f9b039da-2c6b-4f44-b1a3-da7869c6ea47)
![image](https://github.com/user-attachments/assets/08eff37a-7a13-47fd-85b8-5575b67cc296)

## Yumna Khan - Sophomore, Business Analytics and Artificial Intelligence, UTDallas



