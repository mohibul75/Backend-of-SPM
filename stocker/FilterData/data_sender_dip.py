import json, requests, csv, array as arr, pandas as pd, numpy as np

def fetchData(companyId):
    response2 = requests.get(f"https://www.amarstock.com/data/afe01cd8b512070a/?scrip={companyId}&cycle=Day1&dtFrom=2016-12-15T05%3A02%3A13.318Z&fbclid=IwAR0qZBhgiqSV6L6xTerlCEsXvVwtaLMaQvTqqMfUmjloMfBO2jocwV95DE8")
    if (response2.status_code == 200):
        todos2 = json.loads(response2.text)
    json_string = json.dumps(todos2)
    df = pd.read_json(json_string)
    df.sort_values("DateEpoch")
    return df

def getCandleData(companyId):
    df = fetchData(companyId)
    df = df[['DateString', 'Open', 'High', 'Low', 'Close']].dropna()
    df.rename(columns = {'DateString':'x'}, inplace = True)
    df['y'] = df[['Open', 'High', 'Low', 'Close']].values.tolist()
    return list(df[['x', 'y']].T.to_dict().values())

