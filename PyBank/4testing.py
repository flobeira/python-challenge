import os
import csv

budget_data = 'c:/Users/franc/Desktop/UCSD/Homework/python-challenge/PyBank/Resources/budget_data.csv'




with open (budget_data, 'r') as csvfile:

    datareader = csv.reader (csvfile, delimiter = ',')

    header = next(datareader)
    value = len(list(datareader))

    total = 0
    for row in datareader:
        total += float(row[1])
        print(total)





print("Financial Analysis")
print("----------------------------------")

print(f'The total number of months is: {value} ')
print(f'The total Profit is: {total} ')
        
