import requests
import pandas as pd
from sqlalchemy import create_engine

# Fetch data from CoinGecko API
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 5,  # Fetch top 5 coins
    "page": 1,
    "sparkline": "false"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print("API Response:", data[:2])  # Print first 2 items for verification

    # Convert API response to DataFrame
    df = pd.DataFrame(data)[["symbol", "name", "current_price", "market_cap", "total_volume"]]

    # Connect to PostgreSQL
    engine = create_engine('postgresql://postgres:LiA86k:)@localhost:5432/defi_project')


    # Save data to PostgreSQL
    df.to_sql('defi_data', engine, index=False, if_exists='replace')
    print("Data saved to database successfully.")
else:
    print("Error:", response.status_code, response.json())
