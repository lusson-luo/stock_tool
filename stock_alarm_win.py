import urllib.request
import tkinter
import tkinter.messagebox #这个是消息框，对话框的关键
import ctypes
import time
import threading
import logging

stocks = [
{"code":"sz000776","name":"广发证券","min_threshold":"12","max_threshold":"14.89"},
{"code":"sh600383","name":"金的集团","min_threshold":"11.75","max_threshold":"13.16"},
{"code":"sh000016","name":"上证50"}]

def monitor(stock):
	while 1==1:
		time.sleep(5)
		print(f"{stock['name']}股票监控ing...")
		response = str(urllib.request.urlopen(f"http://hq.sinajs.cn/list={stock['code']}").read())
		stockData = response.split("\"")[1].split(",")
		priceNow = stockData[3]
		if stock['min_threshold'] > priceNow:		
			ctypes.windll.user32.MessageBoxA(0,f"{stock['name']}股价跌破设定的最小值{stock['min_threshold']},现在价格为{priceNow}".encode('gb2312'),f"{stock['name']}股价下跌提醒".encode('gb2312'),0)
			break
		if stock['max_threshold'] < priceNow:
			ctypes.windll.user32.MessageBoxA(0,f"{stock['name']}股价突破设定的最大值{stock['max_threshold']},现在价格为{priceNow}".encode('gb2312'),f"{stock['name']}股价上涨提醒".encode('gb2312'),0)
			break

for ind, stock in enumerate(stocks):
	if stock.__contains__('min_threshold') and stock.__contains__('max_threshold'):
		t = threading.Thread(target=monitor,args=(stock, ))
		t.start()
