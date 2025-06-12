# Nifty 50 Historical Data Fetcher via Dhan API
This Python script fetches **daily historical data** for the Nifty 50 index from the [Dhan API](https://dhan.co/) and saves it as a CSV file for further analysis.

## 🚀 Features

- Fetches daily OHLCV (Open, High, Low, Close, Volume) data
- Parses and structures the JSON response into a Pandas DataFrame
- Saves data into a local CSV file (`data.csv`)
- Includes validation to ensure the fetched data is complete
- Supports data visualization and statistical analysis using:
  - `matplotlib`, `seaborn` (for plotting)
  - `scipy.stats` (for skewness, kurtosis calculations – though not yet used)
