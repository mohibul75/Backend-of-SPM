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
    def __init__(self, up, down, unchanged, up_percentage, down_percentage, unchanged_percentage):
        self.up = up
        self.down = down
        self.unchanged = unchanged
        self.up_percentage = up_percentage
        self.down_percentage = down_percentage
        self.unchanged_percentage = unchanged_percentage


def percentage(part, whole):
    percentage = 100 * float(part) / float(whole)
    return percentage


def get_company_statistics():
    arr = []
    response = requests.get(
        "https://www.amarstock.com/LatestPrice/34267d8d73dd?fbclid=IwAR3Nnl2tdnlEuJTOlZgH4yBuQR9ngbSg7y70e_kskcaWqwBfdqSkE7E8-II")
    # print(len(response.json()))
    for item in response.json():
        obj = object(item['FullName'], item['LTP'], item['Close'], item['Change'], item['YCP'])
        # print(json.dumps(obj.__dict__))
        arr.append(json.dumps(obj.__dict__))
    # print(arr)
    return arr
    # print(len(arr))


def get_trade_statistics():
    status_response = requests.get(
        "https://www.amarstock.com/Info/DSE")
    status_response_data = status_response.json()

    total = status_response_data['Advance'] + status_response_data['Decline'] + status_response_data['Unchange']
    stat = status(status_response_data['Advance'], status_response_data['Decline'], status_response_data['Unchange'],
                  percentage(status_response_data['Advance'], total),
                  percentage(status_response_data['Decline'], total),
                  percentage(status_response_data['Unchange'], total))
    # print(json.dumps(stat.__dict__))
    return json.dumps(stat.__dict__)
    stat = status(status_response_data['Advance'], status_response_data['Decline'], status_response_data['Unchange'])

    return stat.__dict__
