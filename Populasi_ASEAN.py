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
querydb = """select Name, Population from country where Region = 'Southeast Asia' order by Name"""
kursor.execute(querydb)

x = kursor.fetchall()
populasi = []
for i in range(len(x)):
    populasi.append(x[i][1])
df = pd.DataFrame(x, columns=['Negara','Populasi'])
plt.style.use('seaborn')
plt.bar(df['Negara'],df['Populasi'], color=['r','b','y','g','k','pink','magenta','brown','cyan','purple','grey'])
plt.xticks(rotation=45)
plt.ylabel('Populasi(x100jt jiwa)')
plt.xlabel('Negara')
plt.title('Populasi Negara ASEAN')
ax = plt.gca()
for i,j in enumerate(populasi):
    plt.text(i-.3,j,str(j),color='black')

plt.show()