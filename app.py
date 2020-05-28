import pandas as pd
import ccxt
import datetime

exchange = ccxt.bitflyer()

def gather_data():
    data = exchange.fetch_ohlcv('BTC/USD', '1s')
    df = pd.DataFrame(data)
    df.columns = (['Date Time', 'Open', 'High', 'Low', 'Close', 'Volume'])

    def parse_dates(ts):
        return datetime.datetime.fromtimestamp(ts/1000.0)
    df['Date Time'] = df['Date Time'].apply(parse_dates)
    df.to_csv('sampledata.csv')


def main():
    gather_data()
    
if __name__ == '__main__':
    main()