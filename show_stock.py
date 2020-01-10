import urllib.request
import sys
import time
import data_read

print("不做短期买入卖出的韭菜操作，跳出周期操作股票，等待3秒出股票价格")
print("安心工作学习，技术才是赚钱根本")
print("买卖股票，\033[31m不应该看股票的价格买卖，而应该分析市场是否有未来，公司是否是龙头\033[0m来买 \n")

time.sleep(3)

show_type = "";
if len(sys.argv) > 1:
    show_type = sys.argv[1]

stocks = data_read.getShowData()

if 'income' == show_type:
    print("name      - now      - max_today      - min_today      - buy_price     - income")
elif '-d' == show_type:
    print("name      - now      - max_today      - min_today")
else:
    print("name      - now      - 抄底价格      - 收网价格")
for ind, stock in enumerate(stocks):
    response = str(urllib.request.urlopen(f"http://hq.sinajs.cn/list={stock.code}").read())
    stockData = response.split("\"")[1].split(",")
    stockName = stockData[0]
    openPrice = stockData[1]
    openPriceYesterday = stockData[2]
    priceNow = stockData[3]
    priceHighest = stockData[4]
    priceLowest = stockData[5]
    if 'income' == show_type and stock.buy_price != 0:
        income=int((float(priceNow) - stock.buy_price) * stock.buy_num)
        print(f"{stock.name}    {priceNow}    {priceHighest}         {priceLowest}            {stock.buy_price}           {income}")
    elif '-d' == show_type:
        print(f"{stock.name}    {priceNow}    {priceHighest}         {priceLowest}")
    else:
        if stock.hope_buy_price != 0:
            print(f"{stock.name}    {priceNow}    {stock.hope_buy_price}         {stock.hope_sell_price}")
        else:
            print(f"{stock.name}    {priceNow}")
