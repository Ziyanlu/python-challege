import os
import csv
poll_csv = os.path.join("Resources", "election_data.csv")
with open(poll_csv, newline ="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)

    rows= []
    candidates= []
    for row in csvreader:
       rows.append(row)
       if row[2] not in candidates:
          candidates.append(row[2])

with open(poll_csv, newline ="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)

    data = {}
    #Initialize the dictionary
    for name in candidates:
        data[name] = 0

    #Count the votes for each candidate
    for row in csvreader:
        data[row[2]] += 1            

print("Election Results")
print("---------------------------")
print(f"Total Votes: {len(rows)}")
print(f"Candidte list : {candidates}")
print("---------------------------")
vote= -100
for name in candidates:  
    if data[name] > vote:
        vote = data[name]
        winner = name
    print(f'{name} {":%.2f%%"%(data[name]/len(rows)*100)} {"("}{str(data[name])}{")"}')    

print("---------------------------")
print(f'{"Winner: "}{winner}')

f= open("txtfile.txt","w")
print("Election Results")
print("---------------------------")
print(f"Total Votes: {len(rows)}")
print(f"Candidte list : {candidates}")
print("---------------------------")
vote= -100
for name in candidates:  
    if data[name] > vote:
        vote = data[name]
        winner = name
    print(f'{name} {":%.2f%%"%(data[name]/len(rows)*100)} {"("}{str(data[name])}{")"}')    

print("---------------------------")
print(f'{"Winner: "}{winner}')
f.close()