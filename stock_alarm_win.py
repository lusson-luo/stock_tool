import urllib.request
import tkinter
import tkinter.messagebox #这个是消息框，对话框的关键
import ctypes
import time
import threading
import logging
from decimal import Decimal

stocks = [
{"code":"sz000776","name":"广发证券","min_threshold":"12","max_threshold":"14.6","min_range":-3,"max_range":3},
{"code":"sh600332","name":"白云山","min_threshold":"33.5","max_threshold":"40","min_range":-3,"max_range":3},
{"code":"sz002415","name":"海康威视","min_threshold":"28.8","max_threshold":"37","min_range":-3,"max_range":3},
{"code":"sh601166","name":"兴业银行","min_threshold":"18","max_threshold":"20","min_range":-2,"max_range":2},
{"code":"sz000002","name":"万科A","min_threshold":"25.5","max_threshold":"28","min_range":-3,"max_range":3},
{"code":"sh600383","name":"金的集团","min_threshold":"12.68","max_threshold":"13.9","min_range":-3,"max_range":3},
{"code":"sh601009","name":"南京银行","min_threshold":"8.58","max_threshold":"11","min_range":-3,"max_range":3},
{"code":"sh601601","name":"中国太保","min_threshold":"35.88","max_threshold":"40","min_range":-2,"max_range":3},
{"code":"sh000016","name":"上证50"}]

def monitor(stock):
	while 1==1:
		time.sleep(5)
		print(f"{stock['name']}股票监控ing...")
		response = str(urllib.request.urlopen(f"http://hq.sinajs.cn/list={stock['code']}").read())
		stockData = response.split("\"")[1].split(",")
		priceNow = stockData[3]
		openPriceYesterday = stockData[2]
		zf = Decimal(100*((float(priceNow)-float(openPriceYesterday))/float(openPriceYesterday))).quantize(Decimal("0.00"))
		if float(stock['min_threshold']) > float(priceNow):		
			ctypes.windll.user32.MessageBoxA(0,f"{stock['name']}股价跌破设定的最小值{stock['min_threshold']},现在价格为{priceNow}".encode('gb2312'),f"{stock['name']}股价下跌提醒".encode('gb2312'),4096)
			break
		if float(stock['max_threshold']) < float(priceNow):
			ctypes.windll.user32.MessageBoxA(0,f"{stock['name']}股价突破设定的最大值{stock['max_threshold']},现在价格为{priceNow}".encode('gb2312'),f"{stock['name']}股价上涨提醒".encode('gb2312'),4096)
			break
		if zf < stock['min_range']:
			ctypes.windll.user32.MessageBoxA(0,f"{stock['name']}股价下跌超过了{stock['min_range']}%,现在价格为{priceNow},下跌了{zf}%".encode('gb2312'),f"{stock['name']}股价当天涨跌幅提醒".encode('gb2312'),4096)
			break
		if zf > stock['max_range']:
			ctypes.windll.user32.MessageBoxA(0,f"{stock['name']}股价上涨超过了{stock['max_range']}%,现在价格为{priceNow},上涨了{zf}%".encode('gb2312'),f"{stock['name']}股价当天涨跌幅提醒".encode('gb2312'),4096)
			break
for ind, stock in enumerate(stocks):
	if stock.__contains__('min_threshold') and stock.__contains__('max_threshold'):
		t = threading.Thread(target=monitor,args=(stock, ))
		t.start()
