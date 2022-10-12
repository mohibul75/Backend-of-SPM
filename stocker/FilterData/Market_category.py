import json
import requests
import datetime

import csv
import array as arr


# def Market_category(id:str):
# 	#pass
# 	companyId = id
# 	response2 = requests.get("https://www.amarstock.com/data/1258dca00155/"+ companyId )
# 	if (response2.status_code == 200):
# 		todos2 = json.loads(response2.text)
# 		if todos2 is None:
# 			return ''
#
# 	response = requests.get("https://www.amarstock.com/LatestPrice/34267d8d73dd?fbclid=IwAR0UNljsm-ezbNkKryoHblOkrZNNzdjUGad6lcqQEydQbKuP7TRbZHYOFr4")
# 	response.raise_for_status()
# 	if (response.status_code == 200):
# 		todos = json.loads(response.text)
# 		#print(todos[0])
# 		companyList = len(todos)
# 		print(companyList)
#
# 		count = 0
# 		all_json_list = {}
#
# 		all_json_list["A"] = []
# 		all_json_list["B"] = []
# 		all_json_list["N"] = []
# 		all_json_list["Z"] = []
# 		all_json_list["null"] = []
#
# 		for x in todos:
#
# 			if (todos2["MarketCategory"]==x["MarketCategory"]):
#
# 				category = ""
#
# 				if (x["MarketCategory"]== "A"):
# 					category= "A"
# 					jdata={
#
#
# 							"CompanyId": x['Scrip'],
# 							"CompanyName": x['FullName'],
#
#
# 					}
# 					all_json_list[category].append(jdata)
#
#
# 				elif (x["MarketCategory"]== "B"):
# 					category= "B"
# 					jdata={
#
#
# 							"CompanyId": x['Scrip'],
# 							"CompanyName": x['FullName'],
#
#
# 					}
# 					all_json_list[category].append(jdata)
#
# 				elif (x["MarketCategory"]== "N"):
# 					category= "N"
# 					jdata={
#
#
# 							"CompanyId": x['Scrip'],
# 							"CompanyName": x['FullName'],
#
#
# 					}
# 					all_json_list[category].append(jdata)
#
# 				elif (x["MarketCategory"]== "Z"):
# 					category= "Z"
# 					jdata={
#
#
# 							"CompanyId": x['Scrip'],
# 							"CompanyName": x['FullName'],
#
#
# 					}
# 					all_json_list[category].append(jdata)
#
# 				elif (x["MarketCategory"]== '' or x["MarketCategory"]== ""):
# 					print(companyId)
# 					category= "null"
# 					jdata={
#
#
# 							"CompanyId": x['Scrip'],
# 							"CompanyName": x['FullName'],
#
#
# 					}
# 					all_json_list[category].append(jdata)
# 					print(jdata)
# 				# print(jdata)
# 				# all_json_list.append(jdata[category])
# 				# all_json_list[category].append(jdata)
# 				# print(all_json_list)
# 				# print("  \n")
# 				# print("  \n")
# 				jdata=""
# 				# count= count+1
#
# 				# if count>10:
# 				# 	break
#
# 	return json.dumps(all_json_list)
#
# #Market_category()
# print(Market_category("BBSCABLES"))

def market_category(id):
    # make this an endpoint
    # this requires changes
    return [{
        "Short_name": "1JANATAMF",
        "Full_name": "First Janata Bank Mutual Fund"
    },
    {
        "Short_name": "1STPRIMFMF",
        "Full_name": "Prime Finance First Mutual Fund"
    },
    {
        "Short_name": "AAMRANET",
        "Full_name": "aamra networks limited"
    },
    {
        "Short_name": "AAMRATECH",
        "Full_name": "aamra technologies limited"
    },
    {
        "Short_name": "ABB1STMF",
        "Full_name": "AB Bank 1st Mutual fund"
    },
    {
        "Short_name": "ABBANK",
        "Full_name": "AB Bank Limited"
    },
    {
        "Short_name": "ACFL",
        "Full_name": "Aman Cotton Fibrous Limited"
    }]


def overall_market_details():
    # make this an endpoint
    to_return = {}
    resp = requests.get("https://www.amarstock.com/Info/DSE")
    data = resp.json()

    now = datetime.datetime.now().year
    resp2 = requests.get(
        f"https://www.amarstock.com/data/afe01cd8b512070a/?scrip=ACI&cycle=Day1&dtFrom={now}-1-1T12:10:11.866Z")
    data2 = resp2.json()

    to_return['TotalTrade'] = data['TotalTrade']
    to_return['TotalVolume'] = data['TotalVolume']
    to_return['TotalValue'] = data['TotalValue']
    to_return['ListedCompanies'] = get_total_companies()
    to_return['TotalTradingDay'] = len(data2)
    to_return['AvgTurnOver'] = round(float(data['TotalValue']) * 1000000 / float(data['TotalTrade']))

    return to_return


def get_total_companies():
    response = requests.get("https://www.amarstock.com/LatestPrice/34267d8d73dd")
    response.raise_for_status()
    if response.status_code == 200:
        todos = json.loads(response.text)
        all_company_list = []
        for x in todos:
            companyId = x['Scrip']
            all_company_list.append(companyId)
    return len(all_company_list)


# print(market_category("sdsd"))
