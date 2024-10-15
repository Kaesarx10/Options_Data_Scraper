# Utilizing Yahoo Finance, and Pandas for this Scraper

import pandas as pd
import yfinance as yf

# Define the Function to Scrape Options Data

def fetch_options_data(ticker):
	"""
	Fetch and display options date for a given stock ticker, and save to a CSV file.
	

	Parameters:
	ticker (str): Stock ticker symbol
	filename(str): Name of the CSV file	

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

# Display test ticker data on terminal

ticker = input('ticket symbol: ')
options_df = fetch_options_data(ticker)
print(options_df.head())

# Save the Data to a CSV file
# A different function to separate saving logic (more modular and simple to maintain).
# Piggy backs on the data from fetch_options_data(ticker)

def fetch_and_save_options_data(ticker, filename):
	"""
	Fetch optionsdata for a given stock ticker and save it to a CSV file.
	
	Parameters:
	ticker (str): stock symbol
	filename (str): Name of the CSV file where to save options data

	returns:
	Print of Options Data on Terminal
	"""
	
	
	options_df = fetch_options_data(ticker)
	options_df.to_csv(filename, index=False)

	print(f"Options data for {ticker} saved to {filename}")
filename = f"{ticker}_options_data.csv"

fetch_and_save_options_data(ticker, filename)
