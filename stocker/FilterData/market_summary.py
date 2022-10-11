import requests

def get_market_summary_datas(company_name):
    dict_data = {}

    url = "https://www.amarstock.com/data/1258dca00155/" + company_name
    response = requests.get(url)
    data = response.json()

    response3 = requests.get("https://www.amarstock.com/info/getreturn?symbol=" + company_name)
    todos3 = response3.json()

    dict_data['YCP'] = data['YCP']
    dict_data['OpenPrice'] = data['OpenPrice']
    dict_data['Q1Eps'] = data['Q1Eps']
    dict_data["Q2Eps"] = data['Q2Eps']
    dict_data['Q3Eps'] = data['Q3Eps']
    dict_data['Q4Eps'] = data['Q4Eps']
    dict_data['Week52Range'] = data['Week52Range']
    dict_data['DayRange'] = data['DayRange']
    dict_data['AuthorizedCap'] = data['AuthorizedCap']
    dict_data['PaidUpCap'] = data['PaidUpCap']
    dict_data['LastAGMHeld'] = data['LastAGMHeld']
    dict_data['ListingYear'] = data['ListingYear']
    dict_data['MarketCategory'] = data['MarketCategory']
    dict_data['Volume'] = data['Volume']
    dict_data['MCCAP'] = data['MarketCap']
    dict_data['6M_Return'] = todos3["6Month"]
    dict_data['1Y_Return'] = todos3["1Year"]
    dict_data['Total_shares'] = data['TotalSecurities']
    dict_data['Credit_rating'] = 'N/A'
    dict_data['Year_end'] = 'June 30'
    dict_data['Debut_trading_date'] = ""


    return dict_data



def market_summary_graph_data(company_name, datefrom):
    dict = []
    url = f"https://www.amarstock.com/data/afe01cd8b512070a/?scrip={company_name}&cycle=Day1&dtFrom={datefrom}"
    response = requests.get(url)
    data = response.json()

    for d in data:
        dict.append({'Close': d["Close"], 'date': d["DateString"]})

    return dict


print(get_market_summary_datas("ACI"))