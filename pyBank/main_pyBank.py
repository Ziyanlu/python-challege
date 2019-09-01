import os
import csv
bank_csv = os.path.join("Resources", "budget_data.csv")
with open(bank_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = "," )
    csvheader = next(csvreader)

    rows= []
    column_1 =[]
    column_2= []
    month_difference =[]
    for row in csvreader:
        rows.append(row)
        column_1.append(row[0])
        column_2.append(int(row[1]))
    
    for i in range(len(row)-1):
        month_difference.append(column_2[i+1]-column_2[i])
    

    sum_number = sum(month_difference)
    mean_number = sum_number/len(rows)
    max_number = max(column_2)
    column_1_max = column_1[column_2.index(max_number)]
    min_number = min(column_2)
    column_1_min = column_1[column_2.index(min_number)]

    print(f"Total Month: {len(rows)}")
    print(f"Total: ${sum_number}")   
    print(f"Average Change: {mean_number}")
    print(f"Greatest Increase in Profits: {column_1_max} {max_number}")
    print(f"Greatest Increase in Profits: {column_1_min} {min_number}")