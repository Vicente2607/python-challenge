#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------


votos=[]
total=0
promedio=0
mayor=0
menor=0
montos=[]
fechas=[]
fechamayor="Ene-2000"
fechamenor="Ene-1999"
votante=[]
condado=[]
candidato=[]
lst2=[]
ganador=0

import os
import csv
csvpath = os.path.join('election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        candidato.append(row[2])
        total=total+1


for i in candidato :
    if i not in lst2:
        lst2.append(i)


for i in lst2:
    veces = candidato.count(i)
    votos.append(veces)
    veces=0


print("Resultado de la Elección")
print("-----------------------------------")
print("Total de Votos "+str(total))
print("-------------------------------------")
j=len(lst2)
for i in range(j):
    print(lst2[i]+": "+"{:.2%}".format(votos[i]/total) +" ("+str(votos[i])+")")

mayor=max(votos)
j=len(votos)
for i in range(j):
    if mayor== votos[i] :
        ganador=i
        break

print("---------------------------------------")
print("El Ganador es: "+ lst2[ganador])

# save the output file path
output_file = os.path.join("poll.txt")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    
    writer = csv.writer(datafile)
    writer.writerow(["Resultado de la Elección"])
    writer.writerow(["--------------------------------------------"])
    writer.writerow(["Total de Votos : "+str(total)])
    writer.writerow(["--------------------------------------------"])
    j=len(lst2)
    for i in range(j):
        writer.writerow( [lst2[i]+": "+"{:.2%}".format(votos[i]/total) +" ("+str(votos[i])+")"])
    writer.writerow(["--------------------------------------------"])
    writer.writerow([" El Ganador es:"+lst2[ganador]])
    writer.writerow(["--------------------------------------------"])

    
   
        
       
    