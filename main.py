# First, you need to install the tvDatafeed library if you haven't already
# pip install --upgrade --no-cache-dir git+https://github.com/rongardF/tvdatafeed.git

from tvDatafeed import TvDatafeed, Interval

# Initialize the data feed
tv = TvDatafeed()

# Fetch the latest Bitcoin price data
# Replace 'BINANCE:BTCUSDT' with the appropriate symbol if needed
bitcoin_data = tv.get_hist(symbol='BTCUSD', exchange='BINANCE', interval=Interval.in_daily, n_bars=10)

print(bitcoin_data)