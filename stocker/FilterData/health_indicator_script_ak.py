import requests
import json


def get_EPS(data):
    eps = data['EPS']
    
    return eps


def get_PE(data):
    audited_PE = data['AuditedPE']
    unaudited_PE = data['UnAuditedPE']
    
    return audited_PE, unaudited_PE


def get_dividend_yield(data):
    dividend_yield = data['DividentYield']
    
    return dividend_yield


def get_PEG_ratio(data, company_name, audited_PE_ratio):
    url = "https://www.amarstock.com/company/a4e5-dd034dc69f8a/?symbol=" + company_name
    response = requests.get(url)
    data = response.json()
    
    eps_initial = data[1]["e"]
    eps_final = data[0]["e"]
    eps_growth = (eps_final - eps_initial)/eps_initial
    PEG_ratio = audited_PE_ratio/eps_growth
    
    return f"{PEG_ratio:.2f}"


def get_dividend_payout_ratio(data):
    dividend_yield = data['DividentYield']
    LTP = data['LastTrade']
    EPS = data['EPS']
    
    dividends_per_share = (dividend_yield * LTP) / 100
    dividend_payout_ratio = dividends_per_share / EPS
    
    return f"{dividend_payout_ratio:.2f}"


def get_health_indicators(company_name):
    dict = []
    dict_data = {}
    
    url = "https://www.amarstock.com/data/1258dca00155/" + company_name
    response = requests.get(url)
    data = response.json()
    
    eps = get_EPS(data)
    audited_PE, unaudited_PE = get_PE(data)   
    PEG_ratio = get_PEG_ratio(data, company_name, audited_PE)       
    dividend_payout_ratio = get_dividend_payout_ratio(data)   
    dividend_yield = get_dividend_yield(data)
    
    dict_data['eps'] = eps
    dict_data['audited_PE'] = audited_PE
    dict_data['unaudited_PE'] = unaudited_PE
    dict_data["PEG_ratio"] = PEG_ratio
    dict_data['dividend_payout_ratio'] = dividend_payout_ratio
    dict_data['dividend_yield'] = dividend_yield

    dict.append(dict_data)

    return dict


xys = get_health_indicators("ACI")
print(xys)
