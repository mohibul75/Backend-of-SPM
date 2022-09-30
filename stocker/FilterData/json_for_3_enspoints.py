import requests
import json

def get_gainer_loser_percentage(x, y, z):
    return f"{(x*100)/(x + y + z):.2f}"

def get_today_value_percentage(num, total):
    return (num*100)/total

def get_yesterday_value_percentage(todays_percentage, yesterdays_value, todays_value):
    return f"{(todays_percentage*yesterdays_value)/todays_value:.2f}"


def todays_value():

    dict = []

    total_value = sum(data['Value'])

    for i in range(len(data['Category'])):
        dict_data = {}
        dict_data["Category"] = data['Category'][i]
        dict_data["Value"] = f"{data['Value'][i]:.1f}"
        dict_data["Percentage"] = f"{get_today_value_percentage(data['Value'][i], total_value):.2f}"
        dict.append(dict_data)

    return dict
  
   
def compare():

    dict = []

    total_todays_value = sum(data['Value'])
    total_yesterday_value = sum(data['YValue'])

    for i in range(len(data['Category'])):
        dict_data = {}
        dict_data["Category"] = data['Category'][i]
        dict_data["Todays_Value"] = f"{data['Value'][i]:.1f}"
        dict_data["Todays_percentage"] = f"{get_today_value_percentage(data['Value'][i], total_todays_value):.2f}"
        dict_data["Yesterdays_Value"] = f"{data['YValue'][i]:.1f}"
        dict_data["Yesterdays_percentage"] = get_yesterday_value_percentage(get_today_value_percentage(data['Value'][i], total_todays_value), data['YValue'][i], data['Value'][i])
        dict.append(dict_data)

    print(dict)
    
    return dict


def gainer_loser():

    dict = []
    
    for i in range(len(data['Category'])): 
        dict_data = {}
        
        dict_data["Category"] = data['Category'][i]
        dict_data["Winner"] = data['Winner'][i]
        dict_data["Winner_percentage"] = get_gainer_loser_percentage(data['Winner'][i], data['Loser'][i], data['Neutral'][i])
        dict_data["Neutral"] = data['Neutral'][i]
        dict_data["Neutral_percentage"] = get_gainer_loser_percentage(data['Neutral'][i], data['Winner'][i], data['Loser'][i])
        dict_data["Loser"] = data['Loser'][i]
        dict_data["Loser_percentage"] = get_gainer_loser_percentage(data['Loser'][i], data['Winner'][i], data['Neutral'][i])
        dict.append(dict_data)


    return dict
    

response = requests.get("https://www.amarstock.com//info/sector/composition")
data = response.json()