# ****************************** Developer Notes ******************************
# This object will both collect and store stock information. These are the
# fields it will need:
#    - What is the stock's symbol? : Str
#    - What is the current price of the stock? : Float
#    - What does the stock pay as a dividend? : Float
#    - Would you like to reinvest your dividends? : Bool
#    - How much will you invest per paycheck towards this stock? : Float
# *****************************************************************************
from __future__ import annotations
from DataConverter import DataConverter

class Stock:

    stockSymbol = ""
    currentPrice = 0.00
    dividend = 0.00
    reinvest = False
    contribution = 0.00

    def __init__(self,
                 stockSymbol,
                 currentPrice,
                 dividend,
                 reinvest,
                 contribution):
        self.stockSymbol = stockSymbol.upper()
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
        currentPrice = float(input("what is the current price of the stock? $"))
        dividend = float(input("What does the stock pay as a dividend? $"))
        reinvest = DataConverter.bool_input("Would you like to reinvest your "\
                                            "dividends? ")
        contribution = float(input("How much would you like to invest in this"\
                                   " stock per paycheck? $"))
        
        return Stock(stockSymbol,
                     currentPrice,
                     dividend,
                     reinvest,
                     contribution)
