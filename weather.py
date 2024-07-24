
import requests

def process_data(data):
    return {"city:": data['name'],"datetime:":data['dt'],"temp:":data['main']['temp'],"humidity: ":data['main']['humidity']}
def get_data(city='New York',appid='d2acd71894f83b9ff42cc7e33d4e09fb'):
 
    URL = "https://api.openweathermap.org/data/2.5/weather"
 
    location = "delhi technological university"
    
    PARAMS = {'q': city,'appid': appid}
 
    r = requests.get(url = URL, params = PARAMS) 
    return process_data(r.json())

print(get_data())




