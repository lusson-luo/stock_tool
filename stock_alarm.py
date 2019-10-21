import urllib.request
import pync

stocks = [{"code":"sz000063","name":"中兴通讯","min_threshold":"30","max_threshold":"34"},{"code":"sh000016","name":"上证50"}]

for ind, stock in enumerate(stocks):
    if stock.__contains__('min_threshold') and stock.__contains__('max_threshold'):
        response = str(urllib.request.urlopen(f"http://hq.sinajs.cn/list={stock['code']}").read())
        stockData = response.split("\"")[1].split(",")
        priceNow = stockData[3]
        if priceNow != '0.000':
            if stock['min_threshold'] > priceNow:
                pync.notify(f'{stock["name"]}当前价格{priceNow}', title=f'{stock["name"]}股票已低于设定值{stock["min_threshold"]}')
            if stock['max_threshold'] < priceNow:
                pync.notify(f'{stock["name"]}当前价格{priceNow}', title=f'{stock["name"]}股票已高于设定值{stock["max_threshold"]}')

    
