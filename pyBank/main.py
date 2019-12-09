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
fechamayor="Ene-2000"
fechamenor="Ene-1999"

import os
import csv
csvpath = os.path.join('budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        fechas.append(row[0])
        montos.append(int(row[1]))
        meses=meses+1
        total=total+int(row[1])

mayor=max(montos)
menor=min(montos)
j=0


for i in montos:
    if mayor==i :
        fechamayor=fechas[j]
    if menor==i :
        fechamenor=fechas[j]
    j=j+1

promedio=(mayor+menor)/2

# save the output file path
output_file = os.path.join("bank.txt")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Analisis Financiero"])
    writer.writerow(["--------------------------------------------"])
    writer.writerow(["Total de meses  : "+str(meses)])
    writer.writerow(["Monto Total     : "+str(total)])
    writer.writerow(["Promedio de Cambios : "+str(promedio)])
    writer.writerow(["El Mayor Profit : " +fechamayor+"  "+str(mayor)])
    writer.writerow(["El Menor Profit : "+fechamenor+"  "+str(menor)])


print("Analisis Financiero")
print("------------------------------------------------------------")
print("Total de meses  : "+str(meses))
print("Monto Total     : "+str(total))
print("Promedio        : "+str(promedio))
print("El Mayor Profit : " +fechamayor+"  "+str(mayor))
print("El Menor Profit : "+fechamenor+"  "+str(menor))


