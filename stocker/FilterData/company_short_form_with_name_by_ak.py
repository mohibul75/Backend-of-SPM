import requests
from bs4 import BeautifulSoup as bs
import urllib.request as ureq

def company_short_form():
    data = []
    
    url = "https://www.amarstock.com/LatestPrice/34267d8d73dd"
    
    response = requests.get(url)
    data = response.json()
    print(len(data))
    
    for i in range(len(data)):
        data_dict = {}
        data_dict['n'] = i
        
        data_dict["Short_name"] = data[i]["Scrip"]
        
        if len(data[i]["FullName"]) < 1:
        
            url2 = "https://www.amarstock.com/data/1258dca00155/" + data_dict["Short_name"]
            response2 = requests.get(url2)
            print(i, " ", response2.status_code)
            
            if response2.status_code == 200:
                data2 = response2.json()
                data_dict["Full_name"] = data2["FullName"]
            # else:
            #     get_url = requests.get(url2)
            #     get_text = get_url.text
            #     soup = bs(get_text, "html.parser")
            #     company = soup.find_all('h1', {'class':'h2 title'})
            #     print("company", company)

        else:
            data_dict["Full_name"] = data[i]["FullName"]
        
        data.append(data_dict)
    
    # print(data)
    return data
    
print(company_short_form())