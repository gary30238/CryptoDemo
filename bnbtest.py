import requests
from datetime import datetime
import pandas as pd
import pytz
import time

# 開始測量
start = time.time()

def get_klines_iter(symbol, interval, start=None, end=None, limit=5000):
    df = pd.DataFrame()
    startDate = end
    url = 'https://api.binance.com/api/v3/klines?symbol=' + \
            symbol + '&interval=' + interval
    if not start is None:
        url = url + '&startTime=' + start

    print(url)
          
    df2 = pd.read_json(url)
    df2.columns = ['Opentime', 'Open', 'High', 'Low', 'Close', 'Volume', 'Closetime', 'Quote asset volume', 'Number of trades','Taker by base', 'Taker buy quote', 'Ignore']
    df2['Opentime'] = pd.to_datetime(df2['Opentime'], unit='ms') + pd.to_timedelta(8, unit='H')
    df2['Closetime'] = pd.to_datetime(df2['Closetime'], unit='ms') + pd.to_timedelta(8, unit='H') 
    df = pd.concat([df2, df], axis=0, ignore_index=True, keys=None)
    df.reset_index(drop=True, inplace=True)
    return df

market = 'BTCUSDT'
tick_interval = '1m'
startTime = str(int(datetime.fromisoformat('2021-06-05 08:00').timestamp()*1000))
endTime = str(int(datetime.fromisoformat('2021-06-05 16:00').timestamp()*1000))

wdf = get_klines_iter(market, tick_interval, '1623205830000')
# 結束測量
end = time.time()
# 輸出結果
print("執行時間：%f 秒" % (end - start))
wdf.to_excel('excel_output.xlsx')
print(wdf)
