import csv
import pandas as pd 

file1 = "bright_stars.csv"
file2 = "unit_converted_stars.csv"

d1=[]
d2=[]

with open (file1,"r",encoding="utf8") as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        d1.append(i)

with open (file2,"r",encoding="utf8") as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        d2.append(i)  

header1 = d1[0]
header2 = d2[0]

h = header1+header2

datad1 = d1[1:]
datad2 = d2[1:]

finaldata = []

for i in datad1:
    finaldata.append(i)

for j in datad2:
    finaldata.append(j)

with open ("totalstars2.csv", "w", encoding="utf8") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)
    csvwriter.writerows(finaldata)

df = pd.read_csv("totalstars2.csv")
df.tail(8)