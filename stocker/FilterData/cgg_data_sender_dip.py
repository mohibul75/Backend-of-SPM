import json, requests, csv, array as arr, pandas as pd, numpy as np
from io import StringIO

def fetchData(companyId):
    response2 = requests.get(f"https://www.amarstock.com/data/1258dca00155/{companyId}?fbclid=IwAR02-1IuXiqgdsEtkfTnWEhPjUsX29tMcMSo_8iFx576_7xYG3r89_v9lQc")
    if (response2.status_code == 200):
        todos2 = json.loads(response2.text)
    return todos2

class CGGData():
    def __init__(self, values) -> None:
        self.ShareHoldingPercentage = values[0]
        self.SponsorDirector = values[1]
        self.Govt = values[2]
        self.Institute = values[3]
        self.Foreign = values[4]
        self.Public = values[5]

def getRequiredColumns(columnNames):
    requiredColumnNames = []
    for columnName in  columnNames:
        if columnName[:-2] in "ShareHoldingPercentage" or columnName[:-2] in "SponsorDirector" or columnName[:-2] in "Govt" or columnName[:-2] in "Institute" or columnName[:-2] in "Foreign" or columnName[:-2] in "Public":
            requiredColumnNames.append(columnName)
    requiredColumnNames = requiredColumnNames[:-1]
    return requiredColumnNames

def createCGGDataObjectArray(data, requiredColumnNames):
    ccgDataObjectArray = []
    iterCount = int(len(requiredColumnNames)/6)
    for i in range(iterCount):
        values = [data[key] for key in requiredColumnNames[i*6:i*6+6]]
        cggData = CGGData(values)
        values = []
        ccgDataObjectArray.append(cggData)
    return ccgDataObjectArray

def getCCGDataObject(companyId):
    data = fetchData(companyId)
    columnNames = list(data.keys())
    requiredColumnNames = getRequiredColumns(columnNames)
    ccgDataObjectArray = createCGGDataObjectArray(data, requiredColumnNames)
    return ccgDataObjectArray

output = getCCGDataObject("BEXIMCO")
print(output)