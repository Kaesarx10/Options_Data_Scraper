# Utilizing Yahoo Finance, and Pandas for this Scraper

import pandas as pd
import yfinance as yf

# Define the Function to Scrape Options Data

def fetch_options_data(ticker):
	"""
	Fetch and display options date for a given  stock ticker.
	

	Parameters:
	ticker (str): Stock ticker symbol
	
	Returns:
	DataFrame: Options data
	"""
# Fetch Stock data

	stock = yf.Ticker(ticker)

# Get Expiration dates
	
	expirations = stock.options

# Fetch Options data for each Expiration

	options_data = []
	
	for expiration in expirations:
		opt = stock.option_chain(expiration)
		calls = opt.calls
		puts = opt.puts
		calls['expirationDate'] = expiration
		puts['expirationDate'] = expiration
		options_data.append(calls)
		options_data.append(puts)

# Combine all options data into a singleDataFrame

	options_df = pd.concat(options_data, ignore_index=True)
	return options_df
