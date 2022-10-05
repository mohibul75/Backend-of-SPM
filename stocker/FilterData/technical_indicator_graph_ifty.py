import json
import requests
import csv
import array as arr
from pprint import pprint
import pandas as pd
from collections import defaultdict


def getMovingAverage(companyId):
    result_ma = {}
    response2 = requests.get(
        f"https://www.amarstock.com/data/afe01cd8b512070a/?scrip={companyId}&cycle=Day1&dtFrom=2016-12-15T05%3A02%3A13.318Z&fbclid=IwAR0qZBhgiqSV6L6xTerlCEsXvVwtaLMaQvTqqMfUmjloMfBO2jocwV95DE8")
    if (response2.status_code == 200):
        todos2 = json.loads(response2.text)
    json_string = json.dumps(todos2)
    df = pd.read_json(json_string)
    # for i in range(len(df)):
    #   if df.loc[i, 'DateEpoch'] == 1483228800000:
    #     print(f"{df.loc[i, 'DateString']}")
    close_p = df[['Close', 'DateString', 'DateEpoch']].copy()
    close_p['SMA12'] = close_p['Close'].rolling(12).mean()
    final_list = close_p[['DateEpoch', 'SMA12']].copy()
    final_list = final_list.dropna()
    final_list.reset_index(inplace=True)
    for i in range(len(final_list)):
        result_ma[str(final_list.loc[i, 'DateEpoch'])] = final_list.loc[i, 'SMA12']
    return result_ma


def getMACD(companyId):
    result_macd = defaultdict(list)
    response2 = requests.get(
        f"https://www.amarstock.com/data/afe01cd8b512070a/?scrip={companyId}&cycle=Day1&dtFrom=2016-12-15T05%3A02%3A13.318Z&fbclid=IwAR0qZBhgiqSV6L6xTerlCEsXvVwtaLMaQvTqqMfUmjloMfBO2jocwV95DE8")
    if (response2.status_code == 200):
        todos2 = json.loads(response2.text)
    json_string = json.dumps(todos2)
    df = pd.read_json(json_string)
    # for i in range(len(df)):
    #   if df.loc[i, 'DateEpoch'] == 1483228800000:
    #     print(f"{df.loc[i, 'DateString']}")
    close_p = df[['Close', 'DateString', 'DateEpoch']].copy()
    # Get the 26-day EMA of the closing price
    k = close_p['Close'].ewm(span=12, adjust=False).mean()
    # Get the 12-day EMA of the closing price
    d = close_p['Close'].ewm(span=26, adjust=False).mean()
    # Subtract the 26-day EMA from the 12-Day EMA to get the MACD
    macd = k - d
    # Get the 9-Day EMA of the MACD for the Trigger line
    macd_s = macd.ewm(span=9, adjust=False).mean()
    # Calculate the difference between the MACD - Trigger for the Convergence/Divergence value
    macd_h = macd - macd_s
    # Add all of our new values for the MACD to the dataframe
    close_p['macd'] = df.index.map(macd)
    close_p['macd_h'] = df.index.map(macd_h)
    close_p['signal'] = df.index.map(macd_s)
    final_macd = close_p[['DateEpoch', 'macd', 'signal', 'macd_h']].copy()
    final_macd = final_macd.dropna()
    final_macd.reset_index(inplace=True)
    for i in range(len(final_macd)):
        result_macd[str(final_macd.loc[i, 'DateEpoch'])].append(final_macd.loc[i, 'macd'])
        result_macd[str(final_macd.loc[i, 'DateEpoch'])].append(final_macd.loc[i, 'signal'])
        result_macd[str(final_macd.loc[i, 'DateEpoch'])].append(final_macd.loc[i, 'macd_h'])
    return result_macd


def getRSI(companyId):
    result_rsi = {}
    response2 = requests.get(
        f"https://www.amarstock.com/data/afe01cd8b512070a/?scrip={companyId}&cycle=Day1&dtFrom=2016-12-15T05%3A02%3A13.318Z&fbclid=IwAR0qZBhgiqSV6L6xTerlCEsXvVwtaLMaQvTqqMfUmjloMfBO2jocwV95DE8")
    if (response2.status_code == 200):
        todos2 = json.loads(response2.text)
    json_string = json.dumps(todos2)
    df = pd.read_json(json_string)
    close_p = df[['Close', 'DateString', 'DateEpoch']].copy()
    # Calculate Price Differences
    close_p['diff'] = close_p['Close'].diff(1)
    # Calculate Avg. Gains/Losses
    close_p['gain'] = close_p['diff'].clip(lower=0).round(2)
    close_p['loss'] = close_p['diff'].clip(upper=0).abs().round(2)

    window_length = 14
    # Get initial Averages
    close_p['avg_gain'] = close_p['gain'].rolling(window=window_length, min_periods=window_length).mean()[
                          :window_length + 1]
    close_p['avg_loss'] = close_p['loss'].rolling(window=window_length, min_periods=window_length).mean()[
                          :window_length + 1]

    # Get WMS averages
    # Average Gains
    for i, row in enumerate(close_p['avg_gain'].iloc[window_length + 1:]):
        close_p['avg_gain'].iloc[i + window_length + 1] = \
            (close_p['avg_gain'].iloc[i + window_length] *
             (window_length - 1) +
             close_p['gain'].iloc[i + window_length + 1]) \
            / window_length
    # Average Losses
    for i, row in enumerate(close_p['avg_loss'].iloc[window_length + 1:]):
        close_p['avg_loss'].iloc[i + window_length + 1] = \
            (close_p['avg_loss'].iloc[i + window_length] *
             (window_length - 1) +
             close_p['loss'].iloc[i + window_length + 1]) \
            / window_length
    # Calculate RS
    close_p['rs'] = close_p['avg_gain'] / close_p['avg_loss']
    # Calculate RSI
    close_p['rsi'] = 100 - (100 / (1.0 + close_p['rs']))
    final_rsi = close_p[['DateEpoch', 'rsi']].copy()
    final_rsi = final_rsi.dropna()
    final_rsi.reset_index(inplace=True)
    for i in range(len(final_rsi)):
        result_rsi[str(final_rsi.loc[i, 'DateEpoch'])] = final_rsi.loc[i, 'rsi']
    return result_rsi


def getdY_MACD_PE(companyId):
    result = defaultdict(list)
    response1 = requests.get(f"https://www.amarstock.com/data/1258dca00155/{companyId}")
    data = response1.json()
    annual_div = (data['DividentYield'] * data['LastTrade']) / 100

    response2 = requests.get(
        f"https://www.amarstock.com/data/afe01cd8b512070a/?scrip={companyId}&cycle=Day1&dtFrom=2016-12-15T05%3A02%3A13.318Z&fbclid=IwAR0qZBhgiqSV6L6xTerlCEsXvVwtaLMaQvTqqMfUmjloMfBO2jocwV95DE8")
    if (response2.status_code == 200):
        todos2 = json.loads(response2.text)
    json_string = json.dumps(todos2)
    df = pd.read_json(json_string)
    modified_df = df.iloc[-5:]
    modified_df.reset_index(inplace=True)
    for i in range(len(modified_df)):
        div_yield = (annual_div / (modified_df.loc[i, 'Close'])) * 100
        # print(div_yield)
        result[str((modified_df.loc[i, "DateEpoch"]))].append(div_yield)
        # ### MACD #####
    response2 = requests.get(
        f"https://www.amarstock.com/data/afe01cd8b512070a/?scrip={companyId}&cycle=Day1&dtFrom=2016-12-15T05%3A02%3A13.318Z&fbclid=IwAR0qZBhgiqSV6L6xTerlCEsXvVwtaLMaQvTqqMfUmjloMfBO2jocwV95DE8")
    if (response2.status_code == 200):
        todos2 = json.loads(response2.text)
    json_string = json.dumps(todos2)
    df = pd.read_json(json_string)
    close_p = df[['Close', 'DateString', 'DateEpoch']].copy()
    # Get the 26-day EMA of the closing price
    k = close_p['Close'].ewm(span=12, adjust=False).mean()
    # Get the 12-day EMA of the closing price
    d = close_p['Close'].ewm(span=26, adjust=False).mean()
    # Subtract the 26-day EMA from the 12-Day EMA to get the MACD
    macd = k - d
    # Get the 9-Day EMA of the MACD for the Trigger line
    macd_s = macd.ewm(span=9, adjust=False).mean()
    # Calculate the difference between the MACD - Trigger for the Convergence/Divergence value
    macd_h = macd - macd_s
    # Add all of our new values for the MACD to the dataframe
    close_p['macd'] = df.index.map(macd)
    close_p['macd_h'] = df.index.map(macd_h)
    close_p['signal'] = df.index.map(macd_s)
    final_macd = close_p[['DateString', 'DateEpoch', 'macd', 'signal']].copy()
    final_macd = final_macd.iloc[-5:]
    final_macd.reset_index(inplace=True)
    for i in range(len(final_macd)):
        result[str(final_macd.loc[i, "DateEpoch"])].append(final_macd.loc[i, "macd"])
    # PE Ratio
    eps = data['EPS']
    for l in range(len(modified_df)):
        pe_ratio = modified_df.loc[l, 'Close'] / eps
        result[str((modified_df.loc[l, 'DateEpoch']))].append(pe_ratio)
    # Return Format is a Dictionary. Key is Date. so result[date] will give you an array of 3 values. First DY, Second MACD, Third PE
    return result
