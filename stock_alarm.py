import urllib.request
import pync
import data_read

stocks = data_read.getAlarmData()

for ind, stock in enumerate(stocks):
    if stock.min_threshold != 0 and stock.max_threshold != 0:
        response = str(urllib.request.urlopen(f"http://hq.sinajs.cn/list={stock.code}").read())
        stockData = response.split("\"")[1].split(",")
        priceNow = float(stockData[3])
        if priceNow != 0.000:
            if stock.min_threshold > priceNow:
                pync.notify(f'{stock.name}当前价格{priceNow}', title=f'{stock.name}股票已低于设定值{stock.min_threshold}')
            if stock.max_threshold < priceNow:
                pync.notify(f'{stock.name}当前价格{priceNow}', title=f'{stock.name}股票已高于设定值{stock.max_threshold}')
