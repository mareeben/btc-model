import pandas as pd


if __name__ == "__main__":
    # Source of date -
    # https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data?select=btcusd_1-min_data.csv

    # Load the data from btcusd_1-min_data.csv
    data = pd.read_csv('./data_raw/btcusd_1-min_data.csv')

    # Ensure the Timestamp column is converted to a datetime format
    data['Timestamp'] = pd.to_datetime(data['Timestamp'], unit='s')

    # Set the Timestamp column as the index
    data.set_index('Timestamp', inplace=True)

    # Resample the data to daily frequency and aggregate values
    daily_data = data.resample('D').agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last', 'Volume': 'sum'})

    # Save the processed daily data to a new CSV file
    daily_data.to_csv('../notebooks/data/btc_usd_kaggle_data.csv')
