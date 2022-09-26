import requests
import json


class RSI:
    def __init__(self, value):
        self.name = "RSI"
        self.value = value
        if value < 30:
            self.Interpretation = "oversold"
            self.verdict = "Buy"


        elif value > 30 and value < 70:
            self.Interpretation = "compare"
            self.verdict = "sell"
        elif value > 70:
            self.Interpretation = "over bought"
            self.verdict = "sell"


class STOC:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        if value < 20:
            self.Interpretation = "oversold"
            self.verdict = "Buy"


        elif value > 20 and value < 80:
            self.Interpretation = "compare"
            self.verdict = "sell"
        elif value > 80:
            self.Interpretation = "over bought"
            self.verdict = "sell"


class MACD:
    def __init__(self, value, MA):
        self.name = "MACD"
        self.value = value
        if value > MA:
            self.Interpretation = "bullish"
            self.verdict = "Buy"


        elif value < MA:
            self.Interpretation = "bearish"
            self.verdict = "sell/neutral"


class technical_indiactors_statistics:
    def __init__(self, Name, Sector, SMA, MACD, ADM, RSI, STOC, OBV, BB):
        self.Name = Name
        self.Sector = Sector
        self.SMA = SMA
        self.MACD = MACD
        self.ADM = ADM
        self.RSI = RSI
        self.STOC = STOC
        self.OBV = OBV
        self.BB = BB


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
    return round(percentage, 2)


def get_company_statistics():
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

    total = status_response_data['Advance'] + status_response_data['Decline'] + status_response_data['Unchange']
    stat = status(status_response_data['Advance'], status_response_data['Decline'], status_response_data['Unchange'],
                  percentage(status_response_data['Advance'], total),
                  percentage(status_response_data['Decline'], total),
                  percentage(status_response_data['Unchange'], total))

    return stat.__dict__


def get_technical_indicators_statistics():
    arr = []
    url = "https://www.amarstock.com/api/grid/scan/simple"
    data = ["MA(12)", "MACD(12,26,9)", "ADX(14)", "RSI(14)", "SO(3,3)", "OBV(20)", "BB(20,2)"]
    response = requests.post(url, json=data)
    for item in response.json():
        rsi = RSI(item['Indi4'])
        stoc = STOC("STOC", item['Indi5'])
        macd = MACD(item['Indi2'], item['Indi1'])
        ma = STOC("SMA", item['Indi1'])
        obj = technical_indiactors_statistics(item['Name'], item['Sector'], ma.__dict__ , macd.__dict__,
                                              item['Indi3'], rsi.__dict__, stoc.__dict__,
                                              item['Indi6'], item['Indi7'])
        arr.append(obj.__dict__)
    return arr


def get_technical_indicators_statistics_of_Company(company_code):
    url = "https://www.amarstock.com/api/grid/scan/simple"
    data = ["MA(12)", "MACD(12,26,9)", "ADX(14)", "RSI(14)", "SO(3,3)", "OBV(20)", "BB(20,2)"]
    response = requests.post(url, json=data)
    for item in response.json():
        rsi = RSI(item['Indi4'])
        stoc = STOC("STOC", item['Indi5'])
        macd = MACD(item['Indi2'], item['Indi1'])
        ma = STOC("SMA", item['Indi1'])
        adm = STOC("ADM", item['Indi3'])
        obv = STOC("OBV", item['Indi6'])
        bb = STOC("BB", item['Indi7'])
        if item['Name'] == company_code:
            obj = technical_indiactors_statistics(item['Name'], item['Sector'], ma.__dict__ , macd.__dict__,
                                                  adm.__dict__, rsi.__dict__, stoc.__dict__,
                                                  obv.__dict__, bb.__dict__)
            return obj.__dict__
        else:
            return None