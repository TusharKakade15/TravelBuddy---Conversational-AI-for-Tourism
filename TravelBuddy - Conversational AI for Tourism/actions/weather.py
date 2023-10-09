import requests

def weather_gen(city):
    # city = input("Enter City:")
    # city=input
    if city==None:
        city = "ghansoli"
    base_url = 'https://api.openweathermap.org/data/2.5/weather?q='
    api="API KEY"
    url=base_url+city+"&appid="+api+"&units=metric"
    res = requests.get(url)
    data = res.json()

    try:
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        description = data['weather'][0]['description']
        temp = data['main']['temp']

        return "Temperature: {}°C\nWind: {} m/s\nPressure: {} hPa\nHumidity: {}%\nWeather Report: {}".format(temp, wind, pressure, humidity, description)

    except KeyError:
        return "Sorry, I could not find the weather information for {}. Please make sure the city name is correct and try again.".format(city)
    # print('Temperature:',temp,'°C')
    # print('Wind:',wind,"m/s",)
    # print('Pressure: ',pressure,"hPa")
    # print('Humidity: ',humidity,"%")
    # print('Weather Report: ',description)