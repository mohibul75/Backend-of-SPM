import json
import requests
import csv
import array as arr

def StaticData():
	#pass
	response = requests.get("https://www.amarstock.com/LatestPrice/34267d8d73dd?fbclid=IwAR0UNljsm-ezbNkKryoHblOkrZNNzdjUGad6lcqQEydQbKuP7TRbZHYOFr4")
	todos = json.loads(response.text)
	#print(todos[0])
	companyList = len(todos)
	print(companyList)

	count = 0
	all_json_list = []

	for x in todos:
		companyId = x['Scrip']
			
		response2 = requests.get("https://www.amarstock.com/data/1258dca00155/"+ companyId +"?fbclid=IwAR12z3-tzoyvn6Fc3Klh1P1U61pPB32RH9ZLD4bWHiWdS2TWWhuy6Thk7-Q")
		todos2 = json.loads(response2.text)

		date= todos2['LastUpdate'].split()

		jdata = {

				"FullName": x['FullName'],
				"LastUpdate": date[0],
				"Details": "",
				"Year_end": todos2['ShareHoldingPercentage2'],
				"Incorporation": "",
				"Commencement_of_operation": "",
				"ListingYear": todos2['ListingYear'],
				"Script_code": todos2['Scrip'],
				"Debut_trading_date": "",
				"Prev_close": todos2['YCP'],
				"OpenPrice": todos2['OpenPrice'],
				"DayRange": todos2['DayRange'],
				"52_weels_range": todos2['Week52Range'],
				"Q1Eps": todos2['Q1Eps'],
				"Q2Eps": todos2['Q2Eps'],
				"Q3Eps": todos2['Q3Eps'],
				"Q4Eps": todos2['Q4Eps'],
				"Authorized_capital": todos2['AuthorizedCap'],
				"MCCAP": todos2['MarketCap'],
				"Total_volume": todos2['Volume'],
				"6M_Return": "",
				"1Y_Return": "",
				"LastAGM": todos2['LastAGMHeld'],
				"Category": todos2['MarketCategory'],
				"Credit_rating": todos2['Rating'],
				"Total_Shares": todos2['TotalSecurities'],
				"Paid_up_CAP": todos2['PaidUpCap'],

		}
		
		all_json_list.append(jdata)
		# count= count+1

		# if count>10:
		# 	break
			
	return json.dumps(all_json_list)
			
print(StaticData())
