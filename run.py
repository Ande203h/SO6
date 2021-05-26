import matplotlib.pyplot as mpl
import calculations as calc

"""
Dokument hvori alle udregningerne der er brugt i opgaven bliver lavet
"""

market = calc.construct_market("symbols.txt", "prices.csv", 2769)
spreadTo2017 = calc.calculate_spread(market, stop = 7*365)
spreadCovid = calc.calculate_spread(market, start = -365, stop = -1)

spreadAverage = calc.interval_spread(market, 365)

print(spreadTo2017)
print(spreadCovid)
print(spreadAverage)

mpl.plot(market)
mpl.show()
