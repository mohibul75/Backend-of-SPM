import json, requests, csv, array as arr, pandas as pd, numpy as np
from io import StringIO

def fetchData(companyId):
    response2 = requests.get(f"https://www.amarstock.com/data/1258dca00155/{companyId}?fbclid=IwAR02-1IuXiqgdsEtkfTnWEhPjUsX29tMcMSo_8iFx576_7xYG3r89_v9lQc")
    if (response2.status_code == 200):
        todos2 = json.loads(response2.text)
    return todos2

def getRequiredColumns(columnNames):
    requiredColumnNames = []
    for columnName in  columnNames:
        if "ShareHoldingPercentage" in columnName or "SponsorDirector" in columnName or "Govt" in columnName or "Institute" in columnName or "Foreign" in columnName or "Public" in columnName:
            requiredColumnNames.append(columnName)
    return requiredColumnNames

def convertDict2DataFrame(data, requiredColumnNames):
    df = pd.DataFrame(columns=['ShareHoldingPercentage', 'SponsorDirector', 'Govt', 'Institute', 'Foreign', 'Public'])
    iterCount = int(len(requiredColumnNames)/6)
    for i in range(iterCount):
        values = [data[key] for key in requiredColumnNames[i*6:i*6+6]]
        df.loc[len(df)] = values
    return df

def getCCGData(companyId):
    data = fetchData(companyId)
    columnNames = list(data.keys())
    requiredColumnNames = getRequiredColumns(columnNames)
    ccgData = dict((key, data[key]) for key in requiredColumnNames)
    ccgData = convertDict2DataFrame(ccgData, requiredColumnNames)
    ccgData.rename(columns = {'ShareHoldingPercentage':'x'}, inplace = True)
    ccgData['y'] = ccgData[['SponsorDirector', 'Govt', 'Institute', 'Foreign', 'Public']].values.tolist()
    return list(ccgData[['x', 'y']].T.to_dict().values())

