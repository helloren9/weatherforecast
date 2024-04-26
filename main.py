import requests

def get_weather(city, units='imperial', api_key='6b0c335914c50cbe5d2194abb3321ca9'):
  url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units={units}&appid={api_key}"
  r = requests.get(url)
  content = r.json()
  with open('data.txt', 'a') as file:
    for wdict in content['list']:
      file.write(f"{content['city']['name']}, {wdict['dt_txt']}, {wdict['main']['temp']}, {wdict['weather'][0]['description']}\n")
  

print(get_weather(city="LasVegas"))
  