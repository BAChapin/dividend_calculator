# ****************************** Developer Notes ******************************
# This is the main entry point for this application. You will run this script
# to start the program.
# *****************************************************************************
from DataCollector import DataCollector

def main():
    investmentData, stocks = DataCollector.run()
    for stock in stocks:
        print(stock)
    else:
        print("*" * 50)
        print(investmentData)

if __name__ == "__main__":
    main()
