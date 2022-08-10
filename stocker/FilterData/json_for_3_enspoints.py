import requests
import json

def get_percentage(x, y, z):
    return f"{(x*100)/(x + y + z):.2f}"

def todays_value():

    dict = []

    for i in range(len(data['Category'])):
        dict_data = {}
        dict_data["Category"] = data['Category'][i]
        dict_data["Value"] = f"{data['Value'][i]:.1f}"
        dict.append(dict_data)

    
    return dict

        
   
def compare():

    dict = []

    for i in range(len(data['Category'])):
        dict_data = {}
        dict_data["Category"] = data['Category'][i]
        dict_data["Todays_Value"] = f"{data['Value'][i]:.1f}"
        dict_data["Yesterdays_Value"] = f"{data['YValue'][i]:.1f}"
        dict.append(dict_data)

    
    return dict


def gainer_loser():

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


    return dict
    

response = requests.get("https://www.amarstock.com//info/sector/composition")
data = response.json()
