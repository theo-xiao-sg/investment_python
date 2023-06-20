import matplotlib.pyplot as plt
import os


def moving_average_strategy(company_name, stock_data, ma_window):

    """
    # calculate the moving average and daily returns
    """

    # Calculate the n-day moving average
    stock_data['moving_average'] = stock_data['price'].rolling(window=ma_window).mean()

    # Calculate the daily returns
    stock_data['daily_return'] = stock_data['price'].pct_change()
    stock_data['daily_return'] = stock_data['daily_return'].fillna(0)

    """
    # calculate the trading signal and signal returns
    """

    # Create a new column to store the trading signal
    stock_data['signal'] = 0

    # Apply the trading signal logic based on n-day moving average
    stock_data.loc[stock_data['price'] >= stock_data['moving_average'], 'signal'] = 1

    # Calculate the daily returns based on the trading signal
    stock_data['signal_return'] = stock_data['daily_return'] * stock_data['signal'].shift(1)
    stock_data['fake_signal_return'] = stock_data['daily_return'] * stock_data['signal'].shift(0)

    """
    # calculate the cumulative returns
    """

    # slice the data to plot pnl from 2020-01-01 to today
    stock_data_slice = stock_data.loc['2020-01-01':]


    # Calculate the cumulative returns
    stock_data_slice['cumulative_signal_return'] = (1 + stock_data_slice['signal_return']).cumprod()
    stock_data_slice['fake_cumulative_signal_return'] = (1 + stock_data_slice['fake_signal_return']).cumprod()

    # Calculate the PnL for the MA strategy, assuming we invest $100
    stock_data_slice['MA_PnL'] = stock_data_slice['cumulative_signal_return'] * 100
    stock_data_slice['fake_MA_PnL'] = stock_data_slice['fake_cumulative_signal_return'] * 100

    # Calculate the PnL for Buy and Hold investment strategy, assuming we invest $100
    stock_data_slice['cumulative_return'] = (1 + stock_data_slice['daily_return']).cumprod()
    stock_data_slice['Buy_Hold_PnL'] = stock_data_slice['cumulative_return'] * 100

    """
    # make plots
    """

    images_folder = 'images'
    os.makedirs(images_folder, exist_ok=True)

    # Plot prices
    plt.plot(stock_data_slice['price'], label='Price')
    plt.title(company_name + ' Prices')
    plt.xlabel('Date')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Price')
    plt.tight_layout()
    plt.grid(True)
    plt.legend()
    plt.show(block=False)
    plt.savefig(r'{}\{}_prices.png'.format(images_folder, company_name))
    plt.close()

    # Plot prices and the moving average
    plt.plot(stock_data_slice['price'], label='Price')
    plt.plot(stock_data_slice['moving_average'], label=str(ma_window)+'-day Moving Average')
    plt.title(company_name + '\nPrices and '+str(ma_window)+'-day Moving Average')
    plt.xlabel('Date')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Price')
    plt.tight_layout()
    plt.grid(True)
    plt.legend()
    plt.show(block=False)
    plt.savefig(r'{}\{}_{}ma.png'.format(images_folder, company_name, str(ma_window)))
    plt.close()

    # Plot the cumulative PnL for both the Buy-Hold and fake MA strategy
    plt.plot(stock_data_slice['Buy_Hold_PnL'], label='Buy_Hold')
    plt.plot(stock_data_slice['fake_MA_PnL'], label='fake_MA')
    plt.title(company_name + '\nComparison of Buy_Hold vs MA Strategies - Cumulative PnL')
    plt.xlabel('Date')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('PnL ($)')
    plt.tight_layout()
    plt.grid(True)
    plt.legend()
    plt.show(block=False)
    plt.savefig(r'{}\{}_{}ma_pnl1.png'.format(images_folder, company_name, str(ma_window)))
    plt.close()

    # Plot the cumulative PnL for both the Buy-Hold and realistic MA strategy
    plt.plot(stock_data_slice['Buy_Hold_PnL'], label='Buy_Hold')
    plt.plot(stock_data_slice['MA_PnL'], label='MA')
    plt.title(company_name + '\nComparison of Buy_Hold vs MA Strategies - Cumulative PnL')
    plt.xlabel('Date')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('PnL ($)')
    plt.tight_layout()
    plt.grid(True)
    plt.legend()
    plt.show(block=False)
    plt.savefig(r'{}\{}_{}ma_pnl2.png'.format(images_folder, company_name, str(ma_window)))
    plt.close()

    # Plot the cumulative PnL for the Buy-Hold and both MA strategies
    plt.plot(stock_data_slice['Buy_Hold_PnL'], label='Buy_Hold')
    plt.plot(stock_data_slice['MA_PnL'], label='MA')
    plt.plot(stock_data_slice['fake_MA_PnL'], label='fake_MA')
    plt.title(company_name + '\nComparison of Buy_Hold vs MA Strategies - Cumulative PnL')
    plt.xlabel('Date')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('PnL ($)')
    plt.tight_layout()
    plt.grid(True)
    plt.legend()
    plt.show(block=False)
    plt.savefig(r'{}\{}_{}ma_pnl3.png'.format(images_folder, company_name, str(ma_window)))
    plt.close()
