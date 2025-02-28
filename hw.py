import sqlite3
import requests
from datetime import datetime
conn = sqlite3.connect('weather.db')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS weather')
cursor.execute('''CREATE TABLE IF NOT EXISTS weather (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    date TEXT, 
                    time TEXT, 
                    temperature TEXT)''')
URL = "https://www.sinoptik.ua/"
response = requests.get(URL)
html = response.text
print(html[:2000])
start_index = html.find('<p class="today-temp">')
if start_index != -1:
    start_index += len('<p class="today-temp">')
    end_index = html.find("&deg;", start_index)
    temperature = html[start_index:end_index]
else:
    temperature = "N/A"
print(f"Температура: {temperature}")
now = datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")
cursor.execute("INSERT INTO weather (date, time, temperature) VALUES (?, ?, ?)", (date, time, temperature))
conn.commit()
conn.close()
print("Дані збережено в базу даних")




