# ****************************** Developer Notes ******************************
# This is the main entry point for this application. You will run this script
# to start the program.
#
# It will first collect the user's information, run the appropriate
# calculations, output the chosen data, and terminate.
# *****************************************************************************
from InvestmentCalculator import InvestmentData, InvestmentCalculator
from DataCollector import DataCollector

def main():
    calculator = InvestmentCalculator(DataCollector.run())
    calculator.run()
    # investmentData = DataCollector.run()

    # investmentData = InvestmentData(12, 5, True, False)
    # print(investmentData.paychecks(1))
    # print(investmentData.paychecks(2))
    # print(investmentData.paychecks(3))
    # print(investmentData.paychecks(4))

    # for stock in stocks:
    #     print(stock)
    # else:
    #     print("*" * 50)
    #     print(investmentData)

if __name__ == "__main__":
    main()
