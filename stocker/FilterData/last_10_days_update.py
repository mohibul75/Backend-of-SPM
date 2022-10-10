import json
import requests
import csv
import array as arr

def Last_ten_days_price_update():
	#pass
	response = requests.get("https://www.amarstock.com/LatestPrice/34267d8d73dd")
	response.raise_for_status()
	if (response.status_code == 200):  
		todos = json.loads(response.text)
		#print(todos[0])
		companyList = len(todos)

		count = 0
		all_json_list = []

		for x in todos:
			companyId = x['Scrip']
			# companyId = "1JANATAMF"
				
			response2 = requests.get("https://www.amarstock.com/data/afe01cd8b512070a/?scrip="+companyId+ "&cycle=Day1&dtFrom=2000-07-20T05%3A02%3A13.318Z" )
			if (response2.status_code == 200):  
				todos2 = json.loads(response2.text)
				if todos2 is None:
					break

				daysLen = len(todos2)

				if (daysLen >= 10):
					
					daysLen=daysLen-1
					ten_days_beforeLen = daysLen -9
					lastDay = todos2[daysLen]["Close"]
					ten_days_before= todos2[ten_days_beforeLen]["Close"]
					result= ten_days_before-lastDay
					value=""
					if (ten_days_before<lastDay):
						value= "up"
					elif (ten_days_before>lastDay):
						value="down"
					elif (ten_days_before==lastDay):
						value="flat"

					jdata = {

							"CompanyId": x['Scrip'],
							"Last_ten_days_update": value,
					}
					all_json_list.append(jdata)
				
	return json.dumps(all_json_list)

print(Last_ten_days_price_update())