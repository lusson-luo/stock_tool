import json
import os

stockDataFiletPath = os.path.abspath(os.path.dirname(__file__)) + "/stock_data.json"

class Stock:
    name = ""
    code = ""
    min_threshold = 0
    max_threshold = 0
    hope_buy_price = 0
    hope_sell_price = 0
    buy_price = 0

    def __init__(self, name, code, min_threshold, max_threshold, hope_buy_price=0, hope_sell_price=0, buy_price=0):
        self.name = name
        self.code = code
        self.min_threshold = min_threshold
        self.max_threshold = max_threshold
        self.hope_buy_price = hope_buy_price
        self.hope_sell_price = hope_sell_price
        self.buy_price = buy_price

def getShowData():
    with open(stockDataFiletPath, 'r') as load_f:
        load_dict = json.load(load_f)
        stocks = map(lambda stock: Stock(stock['name'],
                stock['code'],                             
                stock['min_threshold'] if stock.__contains__('min_threshold') else 0,
                stock['max_threshold'] if stock.__contains__('max_threshold') else 0,
                stock['hope_buy_price'] if stock.__contains__('hope_buy_price') else 0,
                stock['hope_sell_price'] if stock.__contains__('hope_sell_price') else 0,
                stock['buy_price'] if stock.__contains__('buy_price') else 0
            ), load_dict['show_data'])
        return stocks
    return []


def getAlarmData():
    with open(stockDataFiletPath, 'r') as load_f:
        load_dict = json.load(load_f)
        stocks = map(lambda stock: Stock(stock['name'],
                stock['code'],                             
                stock['min_threshold'] if stock.__contains__('min_threshold') else 0,
                stock['max_threshold'] if stock.__contains__('max_threshold') else 0
            ), load_dict['alarm_data'])
        return stocks
    return []
