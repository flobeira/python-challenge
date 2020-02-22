# PyBank In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. 

import os
import csv

file_path = os.path.join("Resources", "budget_data.csv")

def function_1():
    with open(file_path, 'r') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',')
        next(datareader)
        dataList = list(datareader)
    number_of_months = len(dataList)

    # Crete a list specific for the months this will help treat the data as columns, instead of 86 independent strings.
    months = []
    # Create a list sepcific for the Profit/Loss 
    profit_loss = []
    #Use a loop to go through all the 86 strings
    for ii in range(number_of_months):
        month = dataList[ii][0]
        prof_loss = dataList[ii][1]
        #Add the found values to the lists previously create 
        months.append(str(month))
        profit_loss.append(int(prof_loss))

    len(months)
    # Create a variable to add all the values in the Profit/Loss list to print later
    net_profit = sum(profit_loss)

    # Create a new list to store the change in profit
    change_profit = []
    # The range should be one less (-1) than the lenght of the other lists because
    # in order to calculate change we need two values
    for ii in range (len(profit_loss)-1):
        change = profit_loss[ii+1] - profit_loss[ii]
        change_profit.append(change)

    # Using this new list, calculate the change in profit
    average_change = sum(change_profit)/len(change_profit)
    #average_change = round(average_change)
    maxChange = max(change_profit)
    minChange = min(change_profit)

    
    for ii in range(len(change_profit)):
        value = change_profit[ii]
        if value == maxChange:
            max_location = ii
        elif value == minChange:
            min_location = ii


    max_month = months[max_location + 1]
    min_month = months[min_location + 1]

    


    print("Finanacial Analysis")
    print("--------------------------------")

    print("Total month: " + str(number_of_months))
    print("Total: $" + str(net_profit))
    print("Average Change: $"+ str(round(average_change)))
    print("Greatest Increase in Profits: " + max_month + " $"+ str(maxChange))
    print("Greatest Decrease in Profits: " + min_month + " $"+ str(minChange))

#function_1(os.path.join("Resources", "budget_data.csv")
#function_1('c:/Users/franc/Desktop/UCSD/Homework/python-challenge/PyBank/Resources/budget_data.csv')
