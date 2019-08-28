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
df = pd.DataFrame(x, columns=['Negara','Populasi'])
plt.pie(df['Populasi'], labels=df['Negara'], autopct='%.1f%%')
plt.title('Persentase Penduduk ASEAN')
plt.show()