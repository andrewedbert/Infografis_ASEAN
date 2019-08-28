import mysql.connector
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

dbku = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = 'abcdefgh',
    database = 'world'
)

kursor = dbku.cursor()
querydb = """select Name, GNP from country where Region = 'Southeast Asia' order by Name"""
kursor.execute(querydb)
x = kursor.fetchall()
populasi = []
for i in range(len(x)):
    populasi.append(x[i][1])
# print(populasi)
df = pd.DataFrame(x, columns=['Negara','PDB'])
plt.style.use('seaborn')
plt.bar(df['Negara'],df['PDB'])
plt.xticks(rotation=45)
plt.title('Pendapatan Bruto Nasional ASEAN')
plt.xlabel('Negara')
plt.ylabel('Gross National Product (US$)')
ax = plt.gca()

for i,j in enumerate(populasi):
    plt.text(i-.3,j,str(j),color='black')
plt.show()