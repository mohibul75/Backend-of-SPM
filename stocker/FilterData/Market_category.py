import json
import requests
import csv
import array as arr

def Market_category(id:str):
	#pass
	companyId = id
	response2 = requests.get("https://www.amarstock.com/data/1258dca00155/"+ companyId )
	if (response2.status_code == 200):  
		todos2 = json.loads(response2.text)
		if todos2 is None:
			return ''

	response = requests.get("https://www.amarstock.com/LatestPrice/34267d8d73dd?fbclid=IwAR0UNljsm-ezbNkKryoHblOkrZNNzdjUGad6lcqQEydQbKuP7TRbZHYOFr4")
	response.raise_for_status()
	if (response.status_code == 200):  
		todos = json.loads(response.text)
		#print(todos[0])
		companyList = len(todos)
		print(companyList)

        count = 0
        all_json_list = {}

        all_json_list["A"] = []
        all_json_list["B"] = []
        all_json_list["N"] = []
        all_json_list["Z"] = []
        all_json_list["null"] = []

		for x in todos:
			
			if (todos2["MarketCategory"]==x["MarketCategory"]):  

                category = ""
                # print(companyId)

				if (x["MarketCategory"]== "A"):
					category= "A"
					jdata={
						
							
							"CompanyId": x['Scrip'],
							"CompanyName": x['FullName'],
							
						
					}
					all_json_list[category].append(jdata)


				elif (x["MarketCategory"]== "B"):
					category= "B"
					jdata={
						
							
							"CompanyId": x['Scrip'],
							"CompanyName": x['FullName'],
							
						
					}
					all_json_list[category].append(jdata)

				elif (x["MarketCategory"]== "N"):
					category= "N"
					jdata={
						
							
							"CompanyId": x['Scrip'],
							"CompanyName": x['FullName'],
							
						
					}
					all_json_list[category].append(jdata)

				elif (x["MarketCategory"]== "Z"):
					category= "Z"
					jdata={
						
							
							"CompanyId": x['Scrip'],
							"CompanyName": x['FullName'],
							
						
					}
					all_json_list[category].append(jdata)

				elif (x["MarketCategory"]== '' or x["MarketCategory"]== ""):
					print(companyId)
					category= "null"
					jdata={
						
							
							"CompanyId": x['Scrip'],
							"CompanyName": x['FullName'],
							
						
					}
					all_json_list[category].append(jdata)
					print(jdata)
				# print(jdata)
				# all_json_list.append(jdata[category])
				# all_json_list[category].append(jdata)
				# print(all_json_list)
				# print("  \n")
				# print("  \n")
				jdata=""
				# count= count+1

				# if count>10:
				# 	break
				
	return json.dumps(all_json_list)
			
#Market_category()
print(Market_category("BBSCABLES"))