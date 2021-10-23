# ****************************** Developer Notes ******************************
# InvestmentCalculator
#
# InvestmentData
#    - How many paychecks do you receive a year? : Int
#    - How many years would you like to calculate for? : Int
#    - Would you like quarterly print outs? : Bool
#    ? Would you like yearly print outs? : Bool
# *****************************************************************************

class InvestmentCalculator:
    pass


class InvestmentData:
    
    numOfPaychecks = 0
    yearsToCalc = 1
    quarterlyPrint = False
    yearlyPrint = False

    def __init__(self, numOfPaychecks, yearsToCalc, quarterlyPrint, yearlyPrint):
        self.numOfPaychecks = numOfPaychecks
        self.yearsToCalc = yearsToCalc
        self.quarterlyPrint = quarterlyPrint
        self.yearlyPrint = yearlyPrint

    def __str__(self) -> str:
        return "Number of Paychecks: {0}\n"\
               "Years to Calculate: {1}\n"\
               "Quarterly Print Outs: {2}\n"\
               "Yearly Print Outs: {3}".format(self.numOfPaychecks,
                                               self.yearsToCalc,
                                               self.quarterlyPrint,
                                               self.yearlyPrint)
