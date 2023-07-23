import yfinance as yf
from datetime import datetime
from moving_average_strategy import moving_average_strategy

"""
# retrieve historical data from Yahoo Finance
"""

# Define a start date and End Date to retrieve the historical data from Yahoo Finance
start = '2010-01-01'
end = datetime.today().strftime('%Y-%m-%d')

company_name_ticker = {'^NDX': 'Nasdaq 100', 'TSLA': 'Tesla', 'MSFT': 'Microsoft', 'AAPL': 'Apple', 'AMZN': 'Amazon',
                       'goog': 'Google', '0700.HK': 'Tencent', 'NFLX': 'Netflix'}

# Define the ticker symbol for the stocks
# ticker = '^NDX'
# ticker = 'TSLA'
ticker = 'MSFT'
# ticker = 'AAPL'
# ticker = 'AMZN'
# ticker = 'GOOG'
# ticker = '0700.HK'
# ticker = 'NFLX'

# Get the short name of the ticker
company_name = company_name_ticker[ticker]

# Download historical data for the stocks from Yahoo Finance
download_data = yf.download(ticker, start=start, end=end)

"""
# calculate moving average and daily returns
"""

stock_data = download_data[['Close']].copy()
# rename column name to 'price'
stock_data.rename(columns={'Close': 'price'}, inplace=True)

# Calculate the n-day moving average
ma_window = 200

# Call the moving_average_strategy function
moving_average_strategy(company_name, stock_data, ma_window)


print('Done')