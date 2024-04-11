# Import necessary libraries
import streamlit as st
from datetime import date

import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

# Define the start date for historical data and today's date for the end date
START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

# Set the title of the web app
st.title('Stock Forecast App')

# List of stocks to choose from and a dropdown menu for user selection
stocks = ('BRKB',"FXAIX",'NVDA', 'TSM', "V", "VOO")
selected_stock = st.selectbox('Select dataset for prediction', stocks)

# Slider to select the number of years for which to predict the stock prices
n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365

# Function to fetch and load data from Yahoo Finance
@st.cache  # This decorator allows the data to be cached to avoid reloading on every interaction
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

# Load data for the selected stock and notify the user
data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
data_load_state.text('Loading data... done!')

# Display the raw data loaded from Yahoo Finance
st.subheader('Raw data')
st.write(data.tail())

# Function to plot the raw data using Plotly
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

# Plot the raw data
plot_raw_data()

# Preparing the data for forecasting
df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

# Create a Prophet model and fit the data
m = Prophet()
m.fit(df_train)

# Create future dates for the forecast and make predictions
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Display the forecast data and plot the results
st.subheader('Forecast data')
st.write(forecast.tail())
st.write(f'Forecast plot for {n_years} years')
plot_plotly(m, forecast)
