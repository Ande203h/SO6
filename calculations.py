import pandas as pd
import math

def construct_market(indexfile, file, length):
    col_list = [] #makes a list of all the stock symbols
    f = open(indexfile, "r")
    for line in f:
        col_list.append(line.strip())
    f.close()

    #makes a dataFrame of all prices, uses stock symbols as index
    prices = pd.read_csv(file, usecols=col_list)

    #makes a list of stock-average prices, and stores it in a single list, market
    market = []
    for i in range(length):
        market_day = 0
        for j in range(0, len(col_list)):
            n = float(prices[col_list[j]][i])
            market_day += n

        market_day /= len(col_list)
        market.append(market_day)

    return market

def calculate_average(dataset, start=0, stop=0):
    if start >= stop:
        stop = len(dataset)
    avrg = sum(dataset[start:stop]) / len(dataset[start:stop])
    return avrg

def calculate_varians(dataset, start = 0, stop = 0):
    if start >= stop:
        stop = len(dataset)
    dataset_slice = dataset[start:stop]
    avrg = calculate_average(dataset, start, stop)
    varSum = []
    for i in range(len(dataset_slice)):
        varSum.append((dataset_slice[i]-avrg)**2)

    varians = sum(varSum)/len(varSum)
    return varians

def calculate_spread(dataset, start = 0, stop = 0):
    if start >= stop:
        stop = len(dataset)
    spread = math.sqrt(calculate_varians(dataset, start, stop))
    return spread

def interval_spread(dataset, interval): #makes a list of spreads, and averages them
    spread_list = []
    for i in range(int(len(dataset)/interval)):
        spread_list.append(calculate_spread(dataset, start = i*interval, stop = (i+1)*interval))
    return calculate_average(spread_list)
