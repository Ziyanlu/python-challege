import os
import csv
bank_csv = os.path.join("Resources", "budget_data.csv")
with open(bank_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = "," )
    csvheader = next(csvreader)
    
    # row = [row for row in csvreader]
    # print(row[1])
    # print(f"Total Month: {len(row)}")
    
    # number= []
    # for row in csvreader:
    #     number.append (int(row[1]))
    # print(sum(number))


    number= 0
    for row in csvreader:
        number += int(row[1])
    print(number)

    