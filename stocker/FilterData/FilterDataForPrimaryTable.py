class object:
    def __init__(self, trading_code, ltp, closep, change, ycp, ):
        self.trading_code = trading_code
        self.ltp = ltp
        self.closep = closep
        self.change = change
        self.ycp = ycp


def get_response():
    import requests
    import json
    arr = []
    response = requests.get(
        "https://www.amarstock.com/LatestPrice/34267d8d73dd?fbclid=IwAR3Nnl2tdnlEuJTOlZgH4yBuQR9ngbSg7y70e_kskcaWqwBfdqSkE7E8-II")
    #print(len(response.json()))
    for item in response.json():
        obj = object(item['FullName'], item['LTP'], item['Close'], item['Change'], item['YCP'])
        # print(json.dumps(obj.__dict__))
        arr.append(json.dumps(obj.__dict__))
    print(arr)
    #print(len(arr))



if __name__ == '__main__':
    get_response()


