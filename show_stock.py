import urllib.request

stockNos = ["sz000063","sh000016"]
stockNames = ["中兴通讯","上证50"]
print("name      - now      - max_today      - min_today")
for ind, stockNo in enumerate(stockNos):
    response = str(urllib.request.urlopen(f"http://hq.sinajs.cn/list={stockNo}").read())
    stockData = response.split("\"")[1].split(",")
    stockName = stockData[0]
    openPrice = stockData[1]
    openPriceYesterday = stockData[2]
    priceNow = stockData[3]
    priceHighest = stockData[4]
    priceLowest = stockData[5]
    print(f"{stockNames[ind]}    {priceNow}    {priceHighest}         {priceLowest}")
