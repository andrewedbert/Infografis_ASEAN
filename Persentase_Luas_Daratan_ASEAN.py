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
querydb = """select Name, SurfaceArea from country where Region = 'Southeast Asia' order by Name"""
kursor.execute(querydb)
x = kursor.fetchall()
df = pd.DataFrame(x, columns=['Negara','Luas Daratan'])

plt.pie(df['Luas Daratan'], labels=df['Negara'], autopct='%.1f%%')
plt.title('Persentase Luas Daratan ASEAN')
plt.show()