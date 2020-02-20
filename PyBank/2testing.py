import os
import csv

def function_1(file_loc):
    with open(file_loc, 'r') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',')
        header = next(datareader)
        dataList = list(datareader)
    
    number_of_months = len(dataList)
    print("Number of months... " + str(number_of_months))
    months = []
    profit_loss = []
    for ii in range(number_of_months):
        month = dataList[ii][0]
        prof_loss = dataList[ii][1]
        months.append(str(month))
        profit_loss.append(int(prof_loss))

    len(months)

    net_profit = sum(profit_loss)

    change_profit = []
    for ii in range (len(profit_loss)-1):
        change =  -profit_loss[ii]+profit_loss[ii+1]
        change_profit.append(change)

    average_change = sum(change_profit)/len(change_profit)
    maxChange = max(change_profit)
    minChange = min(change_profit)

    for ii in range(len(change_profit)):
        value = change_profit[ii]
        if value == maxChange:
            max_location = ii
        elif value == minChange:
            min_location = ii
    
    max_month = months[max_location + 1]

    print(max_month)



    print(months)
    print(profit_loss)

    print("Net Profit: " + str(net_profit))

    print(change_profit)

    print("average sum "+ str(average_change))


    print(maxChange)
    print(minChange)

function_1('c:/Users/franc/Desktop/UCSD/Homework/python-challenge/PyBank/Resources/budget_data.csv')

