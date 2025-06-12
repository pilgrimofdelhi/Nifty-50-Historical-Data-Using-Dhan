import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis

ACCESS_TOKEN = '' #Enter your access token

# Dhan API endpoint for daily historical data
url = 'https://api.dhan.co/v2/charts/historical'

# Nifty 50 parameters 
security_id = '19'  # Nifty 50 Index (ensure this ID is correct)
exchange_segment = 'IDX_I'
instrument = 'INDEX'
from_date = '2024-01-01'
to_date = '2025-06-11'  # Non-inclusive

# Headers
headers = {
    'Content-Type': 'application/json',
    'access-token': ACCESS_TOKEN
}

# Payload
payload = {
    "securityId": security_id,
    "exchangeSegment": exchange_segment,
    "instrument": instrument,
    "expiryCode": 0,
    "oi": False,
    "fromDate": from_date,
    "toDate": to_date
}

# Fetch daily data
response = requests.post(url, headers=headers, json=payload)
data = response.json()

# Validate and convert data
if all(key in data for key in ('timestamp', 'open', 'high', 'low', 'close', 'volume')):
    df = pd.DataFrame({
        'timestamp': pd.to_datetime(data['timestamp'], unit='s'),
        'open': data['open'],
        'high': data['high'],
        'low': data['low'],
        'close': data['close'],
        'volume': data['volume']
    })

    # Save to CSV
    csv_file_path = "data.csv"
    df.to_csv(csv_file_path, index=False)
    print(f"Data saved to: {csv_file_path}")

else:
    print("Failed to retrieve valid data:", data)
