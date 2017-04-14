"""import os
import pandas as pd
import matplotlib.pyplot as plt


def plot_selected(df, columns, start_index, end_index):
	df.ix[start_index + ':' + end_index, columns]


# Return CSV file path given a ticker symbol
def symbol_to_path(symbol, base_dir='data'):
	return os.path.join(base_dir, '{}.csv'.format(str(symbol)))

# Read stock data (adjusted close) for given symbols from CSV files
def get_data(symbols, dates):
	df = pd.DataFrame(index=dates)

	# Add SPY for reference, if it is absent
	if 'SPY' not in symbols:
			symbols.insert(0, 'SPY')

	for symbol in symbols:
		df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
							  parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
		df_temp = df_temp.rename(columns={'Adj Close': symbol})
		df = df.join(df_temp)

		# Drop dates SPY did not trade
		if symbol == 'SPY':
			df = df.dropna(subset=['SPY'])

	return df

# Plot stock prices
def plot_data(df,title="Stock Prices"):
	ax = df.plot(title=title)
	ax.set_xlabel('Date')
	ax.set_ylabel('Price')
	plt.show()


def test_run():

	# Define a date range
	dates = pd.date_range('2010-01-01', '2010-12-31')

	# CHose stock symbols to read
	symbols = ['GOOG', 'IBM', 'GLD']

	# Slice and plot
	df = get_data(symbols, dates)
	plot_selected(df, ['SPY', 'IBM'], '2010-03-01', '2010-04-01')


test_run()"""