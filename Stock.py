# ****************************** Developer Notes ******************************
# This object will both collect and store stock information. These are the
# fields it will need:
#    - What is the stock's symbol? : Str
#    - What is the current price of the stock? : Float
#    - What does the stock pay as a dividend? : Float
#    - Would you like to reinvest your dividends? : Bool
#    - How much will you invest per paycheck towards this stock? : Float
#
# Add some functionality to calculate a range ±25% the cost of the stock, and
# ±15% dividend earnings.
# *****************************************************************************
from __future__ import annotations
from DataConverter import DataConverter
from math import floor


class Stock:

    stockSymbol = ""
    numOwned = 0
    currentPrice = 0.00
    dividend = 0.00
    reinvest = False
    contribution = 0.00

    totalEarned = 0.00

    def __init__(self,
                 stockSymbol: str,
                 numOwned: int,
                 currentPrice: float,
                 dividend: float,
                 reinvest: bool,
                 contribution: float):
        self.stockSymbol = stockSymbol.upper()
        self.numOwned = numOwned
        self.currentPrice = currentPrice
        self.dividend = dividend
        self.reinvest = reinvest
        self.contribution = contribution

    def __str__(self) -> str:
        return "{0}\n"\
               "Price: ${1:.2f}\n"\
               "Dividend: ${2:.2f}\n"\
               "Reinvest: {3}\n"\
               "Contribution: ${4:.2f}".format(DataConverter.create_header(
                                               self.stockSymbol,
                                               "*",
                                               50),
                                               self.currentPrice,
                                               self.dividend,
                                               self.reinvest,
                                               self.contribution)
    
    @staticmethod
    def collect_input() -> Stock:
        stockSymbol = input("What is the stock's symbol? ")
        numOwned = int(input("How many do you own? "))
        currentPrice = float(input("What is the current price of the stock? $"))
        dividend = float(input("What does the stock pay as a dividend? $"))
        reinvest = DataConverter.bool_input("Would you like to reinvest your "\
                                            "dividends? ")
        contribution = float(input("How much would you like to invest in this"\
                                   " stock per paycheck? $"))
        
        return Stock(stockSymbol,
                     numOwned,
                     currentPrice,
                     dividend,
                     reinvest,
                     contribution)

    def purchase_stocks(self, investment: float) -> tuple(int, float):
        totalStockPurchased = floor(investment / self.currentPrice)
        remainder = investment % self.currentPrice

        self.numOwned += totalStockPurchased

        return (totalStockPurchased, remainder)
    
    def quarterly_dividends(self) -> float:
        return self.numOwned * self.dividend

    def yearly_dividends(self) -> float:
        return self.quarterly_dividends * 4

    def dividend_payout(self) -> float:
        payout = self.quarterly_dividends()
        self.totalEarned += payout

        return payout
