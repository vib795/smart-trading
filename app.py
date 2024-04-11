"""
This module is designed to forecast stock prices using historical data.
It leverages yfinance to fetch the data, Prophet for forecasting, and plotly for visualization.
"""

from datetime import date
import streamlit as st
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('Stock Forecast App')

stocks = ('BRKB',"FXAIX",'NVDA', 'TSM', "V", "VOO")
selected_stock = st.selectbox('Select dataset for prediction', stocks)

n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365

def load_data(ticker):
    """
    Fetch and return stock data from Yahoo Finance.
    
    Args:
        ticker (str): Stock ticker symbol.

    Returns:
        pandas.DataFrame: Stock data.
    """
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
data_load_state.text('Loading data... done!')

st.subheader('Raw data')
st.write(data.tail())

def plot_raw_data(data):
    """
    Plot the raw stock data using Plotly.

    Args:
        data (pandas.DataFrame): Stock data.
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data(data)

df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)

future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

st.subheader('Forecast data')
st.write(forecast.tail())
st.write(f'Forecast plot for {n_years} years')
plot_plotly(m, forecast)
