import requests


def company_short_form():
    data = []
    data_dict = {}
    url = "https://www.amarstock.com/LatestPrice/34267d8d73dd"
    
    response = requests.get(url)
    data = response.json()
    print(len(data))
    
    for i in range(len(data)):
        
        print(data[i]["Scrip"])
        print(data[i]["FullName"])
        

company_short_form()