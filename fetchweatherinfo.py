from datetime import datetime as dt
import requests as rt

key='8f9cfd7ae43e623094c0ffa33851767d'
city=input('Enter name of the city: ')
url= 'http://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}'.format(city, key)

request=rt.get(url)
weather_data=request.json()

if weather_data['cod']=='404':
    print('Invalid City Name')

elif weather_data['cod']==200:    
    
    w_date=dt.now().strftime('%d %b %Y | %I:%M:%S %p')
    w_desc=weather_data['weather'][0]['description']
    w_temp=weather_data['main']['temp']
    w_hum=weather_data['main']['humidity']
    w_speed=weather_data['wind']['speed']

    file=open('weather_data.txt', 'w+')
    file.write('\nWeather Information of {0} on {1}\n'.format(city,w_date))
    file.write('\nWeather Description : {}'.format(w_desc))
    file.write('\nTemperature         : {:.2f} Degrees Celsius'.format(w_temp - 273.15))
    file.write('\nHumidity            : {}%'.format(w_hum))
    file.write('\nWind speed          : {} kmph\n'.format(w_speed))

    file.seek(0)
    print(file.read())
    file.close()

else:
    print('Some error occurred')