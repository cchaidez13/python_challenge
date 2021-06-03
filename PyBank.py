# Modules
import os
import csv

csvpath = os.path.join("python_challenge/budget_data.csv")


with open(csvpath, newline ='') as csvfile:
   
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    print("Analyzing")
    print("---------------------------")
    
    #the total of the months
    header = next(csvreader)
    
    #variables
    count = 0
    total = 0
    average = 0
    current = 0
    highProfit = 0
    highLoss = 0
    ProfitLossdate = ""
    Lossdate = ""
    for row in csvreader:
        total += int(row[1])
        count += 1
        current = int(row[1])
        if(current >= 0): # decide if profit or loss
            if(current > highProfit): #store highest profit date
                highProfit = current
                Profitdate = str(row[0])
        elif(current < 0):
            if(current < highLoss): #store worst loss ever
                highLoss = current
                Lossdate = str(row[0])
average = total / count #average profit over x months
print (total)
    