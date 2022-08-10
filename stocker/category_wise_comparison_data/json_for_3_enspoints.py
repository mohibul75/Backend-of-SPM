import requests
import json

def get_percentage(x, y, z):
    return f"{(x*100)/(x + y + z):.2f}"

def todays_value():
    print("todays value")
    
    dict = []

    for i in range(len(data['Category'])):
        dict_data = {}
        dict_data["Category"] = data['Category'][i]
        dict_data["Value"] = f"{data['Value'][i]:.1f}"
        dict.append(dict_data)
    

    json_object = json.dumps(dict, indent=2)
    print(json.loads(json_object))
    
    return json_object

        
   
def compare():
    print("compare")
    
    dict = []

    for i in range(len(data['Category'])):
        dict_data = {}
        dict_data["Category"] = data['Category'][i]
        dict_data["Todays_Value"] = f"{data['Value'][i]:.1f}"
        dict_data["Yesterdays_Value"] = f"{data['YValue'][i]:.1f}"
        dict.append(dict_data)

    json_object = json.dumps(dict, indent=2)
    print(json.loads(json_object))
    
    return json_object


def gainer_loser():
    print("gainer_loser")
    
    dict = []
    
    for i in range(len(data['Category'])): 
        dict_data = {}
        
        dict_data["Category"] = data['Category'][i]
        dict_data["Winner"] = data['Winner'][i]
        dict_data["Winner_percentage"] = get_percentage(data['Winner'][i], data['Loser'][i], data['Neutral'][i])
        dict_data["Neutral"] = data['Neutral'][i]
        dict_data["Neutral_percentage"] = get_percentage(data['Neutral'][i], data['Winner'][i], data['Loser'][i])
        dict_data["Loser"] = data['Loser'][i]
        dict_data["Loser_percentage"] = get_percentage(data['Loser'][i], data['Winner'][i], data['Neutral'][i])
        dict.append(dict_data)

    json_object = json.dumps(dict, indent=2)
    print(json.loads(json_object))
    
    return json_object
    

response = requests.get("https://www.amarstock.com//info/sector/composition")
data = response.json()
# print(data)

todays_value()
compare()
gainer_loser()