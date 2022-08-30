import json
import requests
import csv

def StaticData():
	#pass
	response = requests.get("https://www.amarstock.com/LatestPrice/34267d8d73dd?fbclid=IwAR0UNljsm-ezbNkKryoHblOkrZNNzdjUGad6lcqQEydQbKuP7TRbZHYOFr4")
	todos = json.loads(response.text)
	#print(todos[0])
	companyList = len(todos)
	print(companyList)

	#for x in range(companyList):
	header = ['CompanyName', 'Date', 'Close']
	with open('companyData.csv', 'w', encoding='UTF8') as f:
		writer = csv.writer(f)
		writer.writerow(header)
		for x in todos:
			#companyId = x['Scrip']
			companyId = "1JANATAMF"
			print(companyId)
			print(x['FullName'])
			print('')
			print('')
			response2 = requests.get("https://www.amarstock.com/data/1258dca00155/"+ companyId +"?fbclid=IwAR12z3-tzoyvn6Fc3Klh1P1U61pPB32RH9ZLD4bWHiWdS2TWWhuy6Thk7-Q")
			todos2 = json.loads(response2.text)

			#for y in todos2:
			#print(x)
			#print(todos2)
				
			#print(x['FullName'])
			date= todos2['LastUpdate'].split()
			#print(date[0])
			#print(todos2['YCP'])
			#print(todos2['OpenPrice'])
			#print(todos2['DayRange'])
			#print(todos2['MarketCap'])
			#print(todos2['Volume'])
			#print(todos2['Week52Range'])
			#print(todos2['ListingYear'])
			#print(todos2['LastAGMHeld'])
			#print(todos2['ListingYear'])
			#print(todos2['MarketCategory'])
			#print(todos2['Rating'])
			#print(todos2['TotalSecurities'])
			#print(todos2['PaidUpCap'])
			#print(todos2['Scrip'])
			#print(todos2['ShareHoldingPercentage2'])
			#print(todos2['AuthorizedCap'])
			#print(todos2['Q1Eps'])
			#print(todos2['Q2Eps'])
			#print(todos2['Q3Eps'])
			#print(todos2['Q4Eps'])
			

				#date= todos2['DateString'].split()

			data=[x['FullName'], date[0], todos2['YCP'], todos2['OpenPrice'], todos2['DayRange'], todos2['MarketCap'], todos2['Volume'], todos2['Week52Range'], todos2['ListingYear'], todos2['LastAGMHeld'], todos2['ListingYear'], todos2['MarketCategory'], todos2['Rating'], todos2['TotalSecurities'], todos2['PaidUpCap'], todos2['Scrip'], todos2['ShareHoldingPercentage2'], todos2['AuthorizedCap'], todos2['Q1Eps'], todos2['Q2Eps'], todos2['Q3Eps'], todos2['Q4Eps'],]
			writer.writerow(data)

			jdata= {

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
			return json.dumps(jdata)
			
print(StaticData())

			#break
			#break

		#print(todos[0])
		#if (x['Scrip'] == '1JANATAMF'):
		#	print(x)

	#
	#print(todos2[1])