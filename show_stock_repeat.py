import urllib.request
import sys
import time
from decimal import Decimal

print("不做短期买入卖出的韭菜操作，跳出周期操作股票，等待3秒出股票价格")
print("安心工作学习，技术才是赚钱根本 \n")
time.sleep(3)

show_income = "";
if len(sys.argv) > 1: 
    show_income = sys.argv[1]

stocks = [
    {"code":"sh600332","name":"白云山","buy_price":24,"buy_num":1000,"hope_buy_price":33,"hope_sell_price":40},
	{"code":"sz000776","name":"广发证券","buy_price":24,"buy_num":1000,"hope_buy_price":11,"hope_sell_price":15},
	{"code":"sh600383","name":"金的集团","buy_price":11.7,"buy_num":1000,"hope_buy_price":11.7,"hope_sell_price":13},
	{"code":"sz000002","name":"万科地产","buy_price":25.5,"buy_num":1000,"hope_buy_price":25.5,"hope_sell_price":30},
	{"code":"sh601166","name":"兴业银行","buy_price":17,"buy_num":1000,"hope_buy_price":17,"hope_sell_price":19},
	{"code":"sz002415","name":"海康威视","buy_price":24,"buy_num":1000,"hope_buy_price":28,"hope_sell_price":40},
    {"code":"sh000016","name":"上证50"}
]

while 1==1 :
	if 'income' == show_income :
		print("name      - now      - max_today      - min_today      - buy_price     - income")
	else :
		print("name      - now         - 涨幅     - 抄底价格      - 收网价格")
	for ind, stock in enumerate(stocks):
		response = str(urllib.request.urlopen(f"http://hq.sinajs.cn/list={stock['code']}").read())
		stockData = response.split("\"")[1].split(",")
		stockName = stockData[0]
		openPrice = stockData[1]
		openPriceYesterday = stockData[2]
		priceNow = stockData[3]
		priceHighest = stockData[4]
		priceLowest = stockData[5]
		zf = str(Decimal(100*((float(priceNow)-float(openPriceYesterday))/float(openPriceYesterday))).quantize(Decimal("0.00"))) + '%'
		if 'income' == show_income and stock.__contains__('buy_price'):
			income = int((float(priceNow) - stock['buy_price']) * stock['buy_num'])
			print(f"{stock['name']}    {priceNow}    {priceHighest}         {priceLowest}            {stock['buy_price']}           {income}")
		elif stock.__contains__('hope_buy_price'):
			print(f"{stock['name']}    {priceNow}       {zf}          {stock['hope_buy_price']}          {stock['hope_sell_price']}")
		else :
			print(f"{stock['name']}    {priceNow}")
		print(f"-----------------------------------------------")
	time.sleep(10)		
    
