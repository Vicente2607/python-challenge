#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)


meses=0
total=0
promedio=0
mayor=0
menor=0
montos=[]
fechas=[]

import os
import csv
csvpath = os.path.join('budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


    mayor=int(row[1])
    menor=mayor
    # Read each row of data after the header
    for row in csvreader:
        fechas.append(row[0])
        montos.append(row[1])
        print(row)
        meses=meses+1
        total=total+int(row[1])

print(str(meses))
print(str(total))
promedio=total/meses
print(str(promedio))
