# ****************************** Developer Notes ******************************
# This object is designed to collect the necessary data from the user. The data
# it will collect is the following:
#    - How many paychecks do you receive a year? : Int
#    - How many years would you like to calculate for? : Int
#    - Would you like quarterly print outs? : Bool
#    ? Would you like yearly print outs? : Bool
#    - Stock Input (This will collect data on the stocks)
#    - Would you like to add another stock? : Bool 
# *****************************************************************************
from InvestmentCalculator import InvestmentData
from DataConverter import DataConverter
from Stock import Stock


class DataCollector:
    
    @staticmethod
    def run() -> InvestmentData:
        numOfPaychecks = int(input("How many paychecks do you receive a "\
                                   "year? "))
        yearsCalculated = int(input("How many years would you like "\
                                    "calculated? "))
        quarterlyPrint = DataConverter.bool_input("Would you like quarterly "\
                                                  "print outs? ")
        yearlyPrint = False
        
        if not quarterlyPrint:
            yearlyPrint = DataConverter.bool_input("Would you like yearly "\
                                                   "print outs? ")

        stocks = DataCollector.__collect_stock()
        investmentData = InvestmentData(numOfPaychecks,
                                        yearsCalculated,
                                        quarterlyPrint,
                                        yearlyPrint,
                                        stocks)

        return investmentData

        
    def __collect_stock() -> list[Stock]:
        """A private method to collect the stocks the user wants to run
        calculations on"""

        continueLoop = True
        stocks = []

        while continueLoop:
            stocks.append(Stock.collect_input())

            continueLoop = DataConverter.bool_input("Would you like to add "\
                                                    "another stock? ")
        else:
            return stocks
