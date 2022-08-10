import requests
import json

class object:
    def __init__(self, trading_code, ltp, closep, change, ycp, ):
        self.trading_code = trading_code
        self.ltp = ltp
        self.closep = closep
        self.change = change
        self.ycp = ycp

class status:
    def __init__(self, up, down, unchanged,):
        self.up = up
        self.down = down
        self.unchanged = unchanged


def get_home_comapny_data():
    arr = []
    response = requests.get(
        "https://www.amarstock.com/LatestPrice/34267d8d73dd?fbclid=IwAR3Nnl2tdnlEuJTOlZgH4yBuQR9ngbSg7y70e_kskcaWqwBfdqSkE7E8-II")
    for item in response.json():
        obj = object(item['FullName'], item['LTP'], item['Close'], item['Change'], item['YCP'])
        arr.append(obj.__dict__)

    return arr

def get_trade_statistics():
    status_response = requests.get(
        "https://www.amarstock.com/Info/DSE")
    status_response_data = status_response.json()
    stat = status(status_response_data['Advance'], status_response_data['Decline'], status_response_data['Unchange'])

    return stat.__dict__



