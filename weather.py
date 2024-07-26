
import requests
import time
import sqlite3

def sqlite_connector():
    con = sqlite3.connect("app.db")
    cur= con.cursor()
    return con,cur
def create_table(con,cur):
    cur.execute("CREATE TABLE IF NOT EXISTS app(name TEXT, datetime TEXT, temp TEXT, humidity TEXT)")
    con.commit()
def insert_data(con,cur,data):
    cur.execute("INSERT INTO app values(?,?,?,?)",tuple([v for k,v in data.items()]))
    con.commit()

def process_data(data):
    return {"city:": data['name'],"datetime:":time.ctime(int(data['dt'])),"temp:":data['main']['temp'],"humidity: ":data['main']['humidity']}
def get_data(city='New York',appid='ENTER YOUR KEY HERE'):
    URL = "https://api.openweathermap.org/data/2.5/weather"    
    PARAMS = {'q': city,'appid': appid}
    r = requests.get(url = URL, params = PARAMS) 
    return process_data(r.json())

con,cur= sqlite_connector()
create_table(con,cur)

while True:
    app_data=get_data('Isfahan')
    insert_data(con,cur,app_data)
    print(app_data)
    time.sleep(5)




