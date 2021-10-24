# ****************************** Developer Notes ******************************
# InvestmentCalculator
#
# InvestmentData
#    - How many paychecks do you receive a year? : Int
#    - How many years would you like to calculate for? : Int
#    - Would you like quarterly print outs? : Bool
#    ? Would you like yearly print outs? : Bool
#    - Stocks
# *****************************************************************************
from __future__ import annotations
from Stock import Stock
from math import floor
import sys


class InvestmentCalculator:
    
    investmentData = None

    # Private Properties
    __quarters = [1, 2, 3, 4]
    __unusedCash = 0.00

    def __init__(self, investmentData: InvestmentData):
        self.investmentData = investmentData

    def run(self):
        for year in range(1, self.investmentData.yearsToCalc + 1):
            self.__calculate_year(year)

    def __calculate_year(self, year: int):
        stockBoughtYear = 0
        divEarnedYear = 0.00

        for quarter in self.__quarters:
            stockBought, earned = self.__calculate_quarter(quarter)
            stockBoughtYear += stockBought
            divEarnedYear += earned
        else:
            if self.investmentData.yearlyPrint:
                # TODO: Once OutputGenerator is created, configure the format
                pass

    def __calculate_quarter(self, quarter: int) -> tuple(int, float):
        stocksBought = 0
        divEarned = 0.00

        for stock in self.investmentData.stocks:
            # Purchase stocks for the quarter
            amount, remainder = stock.purchase_stocks(stock.contribution * self.investmentData.paychecks(quarter))
            self.__unusedCash += remainder
            stocksBought += amount

            # Calculate dividends and reinvest
            dividend = stock.dividend_payout()
            divEarned += dividend
            if stock.reinvest:
                divAmount, divRemainder = stock.purchase_stocks(dividend)
                stocksBought += divAmount
                self.__unusedCash += divRemainder

        else:
            if self.investmentData.quarterlyPrint:
                # TODO: Once OutputGenerator is created, configure the format
                # Old Output: Year & Quarter, Quater's Earnings, and Purchased
                pass

        return stocksBought, divEarned



class InvestmentData:
    
    numOfPaychecks = 0
    yearsToCalc = 1
    quarterlyPrint = False
    yearlyPrint = False
    stocks = []

    def __init__(self, numOfPaychecks: int,
                       yearsToCalc: int,
                       quarterlyPrint: bool,
                       yearlyPrint: bool,
                       stocks: list[Stock]):
        self.numOfPaychecks = numOfPaychecks
        self.yearsToCalc = yearsToCalc
        self.quarterlyPrint = quarterlyPrint
        self.yearlyPrint = yearlyPrint
        self.stocks = stocks

    def __str__(self) -> str:
        return "Number of Paychecks: {0}\n"\
               "Years to Calculate: {1}\n"\
               "Quarterly Print Outs: {2}\n"\
               "Yearly Print Outs: {3}".format(self.numOfPaychecks,
                                               self.yearsToCalc,
                                               self.quarterlyPrint,
                                               self.yearlyPrint)

    def paychecks(self, forQuarterNumber: int) -> int:
        monthlyPaychecks = floor(self.numOfPaychecks / 12)
        quarterlyPaychecks = monthlyPaychecks * 3

        if (self.numOfPaychecks % 12) is 0:
            return quarterlyPaychecks
        else:
            remainder = self.numOfPaychecks % 12

            if forQuarterNumber in [1, 2, 3]:
                return quarterlyPaychecks
            elif forQuarterNumber is 4:
                return quarterlyPaychecks + remainder
            else:
                raise IndexError("Quarter {} is out of bounds".format(forQuarterNumber))
