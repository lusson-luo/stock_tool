import urllib.request
import sys
import time

print("不做短期买入卖出的韭菜操作，\033[31m跳出周期操作股票\033[0m，等待3秒出股票价格")
print("\033[31m安心工作学习，技术才是赚钱根本\033[0m \n")
time.sleep(3)

show_income = "";
if len(sys.argv) > 1: 
    show_income = sys.argv[1]

# {"code":"sz000063","name":"中兴通讯","buy_price":32.4,"buy_num":300,"hope_buy_price":29,"hope_sell_price":36}

stocks = [
    {"code":"sz000063","name":"中兴通讯","hope_buy_price":29,"hope_sell_price":37},
    {"code":"sh600276","name":"恒瑞医药","hope_buy_price":80,"hope_sell_price":''},
    {"code":"sh600036","name":"招商银行","hope_buy_price":35,"hope_sell_price":''},
    {"code":"sz000002","name":"万科 A","hope_buy_price":26,"hope_sell_price":''},
    {"code":"sz000538","name":"云南白药","hope_buy_price":80,"hope_sell_price":''},
    {"code":"sh000016","name":"上证50"}
]

if 'income' == show_income :
    print("name      - now      - max_today      - min_today      - buy_price     - income")
else :
    print("name      - now      - 抄底价格      - 收网价格")
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
    elif stock.__contains__('hope_buy_price'):
        print(f"{stock['name']}    {priceNow}    {stock['hope_buy_price']}         {stock['hope_sell_price']}")
    else :
        print(f"{stock['name']}    {priceNow}")
    
