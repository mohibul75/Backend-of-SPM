import json
import requests
import csv
import array as arr


# def report_with_news(id):
#     # pass
#     # response = requests.get("https://www.amarstock.com/LatestPrice/34267d8d73dd?fbclid=IwAR0UNljsm-ezbNkKryoHblOkrZNNzdjUGad6lcqQEydQbKuP7TRbZHYOFr4")
#     # response.raise_for_status()
#     # if (response.status_code == 200):
#     # 	todos = json.loads(response.text)
#     # 	#print(todos[0])
#     # 	companyList = len(todos)
#     # 	print(companyList)
#
#     # 	count = 0
#     # all_json_list = []
#
#     # for x in todos:
#     companyId = id
#     jdata = {}
#     # companyId = "BBSCABLES"
#
#     response2 = requests.get("https://www.amarstock.com/data/1258dca00155/" + companyId)
#     response3 = requests.get("https://www.amarstock.com/company/8821-633c4375ac25/?symbol=" + companyId)
#     if (response2.status_code == 200 and response3.status_code == 200):
#         todos2 = json.loads(response2.text)
#         todos3 = json.loads(response3.text)
#         if todos2 is None or todos3 is None:
#             return {}
#
#         reportLen = len(todos3)
#         print(reportLen)
#
#         jdata = {
#
#             "news1sttitle": todos2['news1sttitle'],
#             "news1stbody": todos2['news1stbody'],
#             "news2sttitle": todos2['news2sttitle'],
#             "news2stbody": todos2['news2stbody'],
#             "news3sttitle": todos2['news3sttitle'],
#             "news3stbody": todos2['news3stbody'],
#             "news4sttitle": todos2['news4sttitle'],
#             "news4stbody": todos2['news4stbody'],
#             "news5sttitle": todos2['news5sttitle'],
#             "news5stbody": todos2['news5stbody'],
#
#         }
#         num = 1
#
#         for y in todos3:
#             titl = "title-" + str(num)
#             filePth = "filePath-" + str(num)
#             # print(y["Title"],y["FilePath"])
#             # print(titl, filePth)
#             newData = {
#                 titl: y["Title"],
#                 filePth: "https://file.amarstock.com/" + y["FilePath"]
#             }
#             jdata.update(newData)
#             # filePath= {filePth : y["FilePath"]}
#             # jdta= json.loads(jdata)
#             # jdta.update(title)
#             # # jdata.update(filePath)
#             # jdata = jdta
#             num += 1
#
#     # print(jdata)
#     # print("\n\n")
#     # break
#     # all_json_list.append(jdata)
#     # count= count+1
#
#     # if count>10:
#     # 	break
#
#     return jdata


# Report_with_news()
# print(report_with_news("BEACONPHAR"))

def report_with_news(id):
    return {
        "news": [
            {
                "title:": "Share Transmission of Deceased Director among his successors",
                "body": "Referring to the BSEC letter No. SEC/SRMIC/94-36/287 dated June 30, 2022, the Company has "
                        "informed that Mrs. Najma Dowla, one of the Directors of the company passed away on "
                        "28.07.2021. Her total holding 20,06,645 shares will be transmitted among his successors "
                        "according to the Succession Certificate issued by the Honorable Court. "
            },
            {
                "title": "Arrangement for Demerger and Merger subject to proper authorities' approval",
                "body": "(Continuation news of ACI):  under the provision of Section 228 & 229 of the Companies Act "
                        "1994 subject to the consent of Shareholders and Creditors of the respective companies and "
                        "approval from the Honorable High Court Division of Supreme Court of Bangladesh to create "
                        "distinct brand identity for ACI Premio Plastics Limited for the consumer and to connect the "
                        "backward linkage operation of Premiaflex Plastics Limited to the Company. "
            }
        ],
        "reports": [
            {
                "title": f"{id}-2018-2019-q1",
                "link": "https://file.amarstock.com/" + "Content/scripReport/Quarterly/aci-2018-2019-q1-7439955496.pdf",
                "type": "Quarterly"
            },
            {
                "title": f"{id}-2019-2020-q1",
                "link": "https://file.amarstock.com/" + "Content/scripReport/Quarterly/aci-2018-2019-q1-7439955496.pdf",
                "type": "Annual"
            }
        ]
    }


