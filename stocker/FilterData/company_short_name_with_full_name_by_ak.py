import requests
import json
import urllib.request as ureq

def company_short_form_generator():
    list_of_company_name_and_short_name = []
    
    url = "https://www.amarstock.com/LatestPrice/34267d8d73dd"
    
    response = requests.get(url)
    data = response.json()
    
    for i in range(len(data)):
        data_dict = {}        
        data_dict["Short_name"] = data[i]["Scrip"]
        
        if len(data[i]["FullName"]) < 1:
        
            url2 = "https://www.amarstock.com/data/1258dca00155/" + data_dict["Short_name"]
            response2 = requests.get(url2)
            
            if response2.status_code == 200:
                data2 = response2.json()
                data_dict["Full_name"] = data2["FullName"]

        else:
            data_dict["Full_name"] = data[i]["FullName"]
        
        list_of_company_name_and_short_name.append(data_dict)
        if i > 380:
            print(i)
    
    return list_of_company_name_and_short_name


# json_object = json.dumps(company_short_form_generator(), indent=4)  
# with open("company_name_with_short_name2.json", "w") as outfile:
#     outfile.write(json_object)
# print(company_short_form())


def get_company_short_name():
    with open('stocker\FilterData\company_name_with_short_name.json', 'r') as openfile:
         json_object = json.load(openfile)

    return json_object
