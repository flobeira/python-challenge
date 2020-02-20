# PyBank In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. 

import os
import csv

budget_data = 'c:/Users/franc/Desktop/UCSD/Homework/python-challenge/PyBank/Resources/budget_data.csv'

def calculations (Data):

    month = str(Data[0])
    profit_loss = int(Data[1])
        #for ii in range(len(Data))

    print(month)
    print(profit_loss)

    print("------------------------------")


with open (budget_data, 'r') as csvfile:

    datareader = csv.reader(csvfile, delimiter = ',')

    header = next(datareader)
    dataList = list(datareader)
    print(dataList)
    num = len(dataList)
    print(num)
    #for go in dataList:
            #calculations(go)
            #break

