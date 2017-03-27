import pandas as pd

def test_run():
	start_date = '2010-01-22'
	end_date = '2010-01-26'
	dates = pd.date_range(start_date,end_date)

	# Create dataframe with list of dates between start & end
	df1 = pd.DataFrame(index=dates)

	# Read SPY data into temporary dataframe
	dfSPY = pd.read_csv('data/SPY.csv', index_col="Date",
						parse_dates=True, usecols=['Date','Adj Close'],
						na_values=['nan'])

	# join the two dataframes using DataFrame.join(), with how='inner'
	# df1 = df1.join(dfSPY)
	# df1 = df1.dropna()
	df1 = df1.join(dfSPY,how='inner')

	# Read in more stocks
	symbols = ['GOOG','IBM','GLD']
	for symbol in symbols:
		df_temp = pd.read_csv("data/{}.csv".format(symbol), index_col="Date",
							  parse_dates=True, usecols=['Date','Adj Close'],
							  na_values=['nan'])
		df_temp = df_temp.rename(columns={'Adj Close': symbol})
		df1 = df1.join(df_temp) # use a defaul how='left'

	print(df1)

test_run()