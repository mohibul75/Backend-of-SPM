import json
import requests
import csv
import array as arr

def Report_with_news():
	#pass
	response = requests.get("https://www.amarstock.com/LatestPrice/34267d8d73dd?fbclid=IwAR0UNljsm-ezbNkKryoHblOkrZNNzdjUGad6lcqQEydQbKuP7TRbZHYOFr4")
	response.raise_for_status()
	if (response.status_code == 200):  
		todos = json.loads(response.text)
		#print(todos[0])
		companyList = len(todos)
		# print(companyList)

		count = 0
		all_json_list = []

		for x in todos:
			# companyId = x['Scrip']
			companyId = "BBSCABLES"
				
			response2 = requests.get("https://www.amarstock.com/data/1258dca00155/"+ companyId )
			response3 = requests.get("https://www.amarstock.com/company/8821-633c4375ac25/?symbol=" + companyId )
			if (response2.status_code == 200 and response3.status_code == 200):  
				todos2 = json.loads(response2.text)
				todos3 = json.loads(response3.text)
				if todos2 is None or todos3 is None:
					break

				reportLen = len(todos3)
				# print(reportLen)

				jdata = {

						
						"news1sttitle": todos2['news1sttitle'],
						"news1stbody": todos2['news1stbody'],
						"news2sttitle": todos2['news2sttitle'],
						"news2stbody": todos2['news2stbody'],
						"news3sttitle": todos2['news3sttitle'],
						"news3stbody": todos2['news3stbody'],
						"news4sttitle": todos2['news4sttitle'],
						"news4stbody": todos2['news4stbody'],
						"news5sttitle": todos2['news5sttitle'],
						"news5stbody": todos2['news5stbody'],
						

				}
				num = 1
				

				for y in todos3:
					titl= "title-"+ str(num)
					filePth = "filePath-"+ str(num)
					# print(y["Title"],y["FilePath"])
					# print(titl, filePth)
					newData= {
						titl : y["Title"],
						filePth : y["FilePath"]
					}
					jdata.update(newData)
					# filePath= {filePth : y["FilePath"]}
					# jdta= json.loads(jdata)
					# jdta.update(title)
					# # jdata.update(filePath)
					# jdata = jdta
					num += 1


				# print(jdata)
				# print("\n\n")
				# break
				all_json_list.append(jdata)
				# count= count+1

				# if count>10:
				# 	break
				
	return json.dumps(all_json_list)
			
print(Report_with_news())
