import json
import requests
import csv
import array as arr

def company_description(id):
	#pass
	# response = requests.get("https://www.amarstock.com/LatestPrice/34267d8d73dd?fbclid=IwAR0UNljsm-ezbNkKryoHblOkrZNNzdjUGad6lcqQEydQbKuP7TRbZHYOFr4")
	# response.raise_for_status()
	# if (response.status_code == 200):  
	# 	todos = json.loads(response.text)
	# 	#print(todos[0])
	# 	companyList = len(todos)
	# 	print(companyList)

	# 	count = 0
	# all_json_list = []

	
	companyId = id
	url = "https://www.amarstock.com/data/1258dca00155/" + companyId			
	response2 = requests.get(url)
	jdata = {}
	if (response2.status_code == 200):  
		todos2 = json.loads(response2.text)
		if todos2 is None:
			return ""

		details = todos2['FullName'] + ", also know by it's trading code "+ companyId +", is one of the leading securities in Dhaka Stock Exchange. This company can be reached at the following contact details - "

		jdata = {

				"CompanyId": todos2['Scrip'],
				"Details": details,						
				"Contact": todos2['Contact'],
				"Email": todos2['Email'],
				"Address": todos2['Address'],
						

		}
		#print(jdata)
		# all_json_list.append(jdata)
				# count= count+1

				# if count>10:
				# 	break
				
	return jdata
			
#Company_description()
# print(company_description("ACI"))
