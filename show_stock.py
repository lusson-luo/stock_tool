import urllib.request
import sys

show_income = "";
if len(sys.argv) > 1: 
    show_income = sys.argv[1]

stocks = [
    {"code":"sz000063","name":"中兴通讯","buy_price":28.40,"buy_num":400},
    {"code":"sh000016","name":"上证50"}
]

print(f"show_income : {show_income}")

if 'income' == show_income :
    print("name      - now      - max_today      - min_today      - buy_price     - income")
else :
    print("name      - now      - max_today      - min_today")
for ind, stock in enumerate(stocks):
    response = str(urllib.request.urlopen(f"http://hq.sinajs.cn/list={stock['code']}").read())
    stockData = response.split("\"")[1].split(",")
    stockName = stockData[0]
    openPrice = stockData[1]
    openPriceYesterday = stockData[2]
    priceNow = stockData[3]
    priceHighest = stockData[4]
    priceLowest = stockData[5]
    if 'income' == show_income and stock.__contains__('buy_price'):
        income = int((float(priceNow) - stock['buy_price']) * stock['buy_num'])
        print(f"{stock['name']}    {priceNow}    {priceHighest}         {priceLowest}            {stock['buy_price']}           {income}")
    else :
        print(f"{stock['name']}    {priceNow}    {priceHighest}         {priceLowest}")
    
