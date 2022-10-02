import json, requests, csv, array as arr, pandas as pd, numpy as np
from pprint import pprint

#fetch data of a specific company
def fetchData(companyId):
    response2 = requests.get(f"https://www.amarstock.com/data/afe01cd8b512070a/?scrip={companyId}&cycle=Day1&dtFrom=2016-12-15T05%3A02%3A13.318Z&fbclid=IwAR0qZBhgiqSV6L6xTerlCEsXvVwtaLMaQvTqqMfUmjloMfBO2jocwV95DE8")
    if (response2.status_code == 200):
        todos2 = json.loads(response2.text)
    json_string = json.dumps(todos2)
    df = pd.read_json(json_string)
    df.sort_values("DateEpoch")
    return df

def getBollingerBand(companyId):
    df = fetchData(companyId)
    df = df[['High', 'Low', 'Close', 'DateString', 'DateEpoch']].copy()
    df['TP'] = (df['High'] + df['Low'] + df['Close'])/3
    df['SMA20'] = df['TP'].rolling(20).mean()
    df['STD20'] = df['TP'].rolling(20).std()
    m = 2
    df['BOLU'] = df['SMA20'] + m*df['STD20']
    df['BOLD'] = df['SMA20'] - m*df['STD20']
    df = df[['DateEpoch', 'BOLU', 'BOLD']].dropna()
    return list(df.T.to_dict().values())


def getStochastic(companyId):
    df = fetchData(companyId)
    df = df[['High', 'Low', 'Close', 'DateString', 'DateEpoch']].copy()
    df['LowestLow14'] = df['Low'].rolling(14).min()
    df['HighestHigh14'] = df['High'].rolling(14).max()
    df['Stochastic'] = (df['Close'] - df['LowestLow14'])/(df['HighestHigh14'] - df['LowestLow14']) * 100
    df = df[['DateEpoch', 'Stochastic']].dropna()
    return list(df.T.to_dict().values())


def calculateADX(df: pd.DataFrame(), interval: int=14):
    df['-DM'] = df['Low'].shift(1) - df['Low']
    df['+DM'] = df['High'] - df['High'].shift(1)
    df['+DM'] = np.where((df['+DM'] > df['-DM']) & (df['+DM']>0), df['+DM'], 0.0)
    df['-DM'] = np.where((df['-DM'] > df['+DM']) & (df['-DM']>0), df['-DM'], 0.0)
    df['TR_TMP1'] = df['High'] - df['Low']
    df['TR_TMP2'] = np.abs(df['High'] - df['AdjClose'].shift(1))
    df['TR_TMP3'] = np.abs(df['Low'] - df['AdjClose'].shift(1))
    df['TR'] = df[['TR_TMP1', 'TR_TMP2', 'TR_TMP3']].max(axis=1)
    df['TR'+str(interval)] = df['TR'].rolling(interval).sum()
    df['+DMI'+str(interval)] = df['+DM'].rolling(interval).sum()
    df['-DMI'+str(interval)] = df['-DM'].rolling(interval).sum()
    df['+DI'+str(interval)] = df['+DMI'+str(interval)] /   df['TR'+str(interval)]*100
    df['-DI'+str(interval)] = df['-DMI'+str(interval)] / df['TR'+str(interval)]*100
    df['DI'+str(interval)+'-'] = abs(df['+DI'+str(interval)] - df['-DI'+str(interval)])
    df['DI'+str(interval)] = df['+DI'+str(interval)] + df['-DI'+str(interval)]
    df['DX'] = (df['DI'+str(interval)+'-'] / df['DI'+str(interval)])*100
    df['ADX'] = df['DX'].rolling(interval).mean()
    df['ADX'] =   df['ADX'].fillna(df['ADX'].mean())
    del df['TR_TMP1'], df['TR_TMP2'], df['TR_TMP3'], df['TR'], df['TR'+str(interval)]
    del df['+DMI'+str(interval)], df['DI'+str(interval)+'-']
    del df['DI'+str(interval)], df['-DMI'+str(interval)]
    del df['+DI'+str(interval)], df['-DI'+str(interval)]
    del df['DX']
    return df


def getAverageDirectionalIndex(companyId):
    df = fetchData(companyId)
    df = calculateADX(df)
    df = df[['DateEpoch', 'ADX']].dropna()
    return list(df.T.to_dict().values())


def getOBV(companyId):
    df = fetchData(companyId)
    df = df[['Close', 'Volume', 'DateString', 'DateEpoch']].copy()
    df['OBV'] = np.where(df['Close'] > df['Close'].shift(1), df['Volume'],
                np.where(df['Close'] < df['Close'].shift(1), -df['Volume'], 0)).cumsum()
    df = df[['DateEpoch', 'OBV']].dropna()
    return list(df.T.to_dict().values())

