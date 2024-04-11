# Stock Forecast App

This app is designed to help traders and investors make informed decisions by predicting stock prices using historical data. It leverages powerful libraries like Prophet, yfinance, and Plotly to provide visual forecasts and insights.

## Overview

Trading involves the buying and selling of financial instruments, aiming to profit from market movements. Traders often spend extensive time analyzing various dashboards to make optimal buy or sell decisions. This app automates the analysis process, offering predictions on stock prices based on historical data from Yahoo Finance, making it easier for traders to plan their moves.

## Features

- **Algo Trading**: Automate trading decisions based on predictive analysis.
- **Stock Price Comparison Dashboard**: Visually compare historical and forecasted data of selected stocks.

## Installation

To run this app, you need to install several Python libraries including Streamlit for web app functionality, yfinance for fetching historical stock data, Prophet for making time series predictions, and Plotly for interactive charts.

```bash
pip install streamlit prophet yfinance plotly
```

## Usage
After installing the necessary libraries, you can run the app using the following command:
```bash
streamlit run app.py
```

This will start a local server, usually on http://localhost:8501, where the app can be accessed through a web browser.

## How It Works
- Data Fetching: The app fetches historical stock data using yfinance based on user-selected stocks.
- Data Visualization: Displays raw historical data and allows for interactive exploration.
- Forecasting: Utilizes Prophet to forecast future stock prices. Users can select the number of years for prediction.
- Result Visualization: Provides visual charts of both historical and predicted data using Plotly.

## Contributing
Feel free to fork this repository, make changes, and submit pull requests if you have improvements or new features you would like to add. We appreciate contributions from the community!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer
This tool is for educational and informational purposes only. Always do your own research before making any trading or investment decisions.