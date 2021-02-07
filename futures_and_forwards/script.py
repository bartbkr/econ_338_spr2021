"""
Examples of futures pricing
"""
import os
import yfinance

import numpy as np

from fredapi import Fred

# SEC: Pull down T-Bill data
fred = Fred(api_key=os.environ['FRED_API_KEY'])
t_bill_3m = fred.get_series('TB3MS')
# SEC: Let's work with GOOGL
gold = yfinance.Ticker('GC=F')
# DOC: Some general info on ticker
print(gold.info.keys())
# DOC: Now let's write a function for calculating no-arbitrage futures price
risk_free_return = 55 - (50 * np.exp(0.09 * 0.25))

def futures_price_no_arbitrage(underlying_spot, risk_free_rate,
                               time_to_delivery):
    """
    Calculates price of futures contract under no-arbitrage conditions

    Parameters
    ----------
    underlying_spot : float
        The spot price of the underlying today.
    risk_free_rate : float
        Risk-free rate locked in over time to delivery
    time_to_delivery : float
        Time to delivery
    Returns
    -------
    Futures price

    """
    return underlying_spot * np.exp(risk_free_rate * time_to_delivery)

futures_price = futures_price_no_arbitrage(50, 0.09, 3 / 12)
print("No arbitrage futures price is: " + str(futures_price))

# SEC: Code
gold.history(start='2000-01-01')
