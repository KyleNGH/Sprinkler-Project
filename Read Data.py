'''
Date: Nov 26, 2018
Name: Kyle GH
File: Read Data from file

'''

### pull current weather 
def get_weather():
    import pyowm

    # api key
    owm = pyowm.OWM("b508f902bfd4f9d38491e1b8557c675f")

    observation = owm.weather_at_place("Honolulu,us")

    weather = observation.get_weather()

    status = weather.get_status()
    
    return status



### main ###

status = get_weather()
print(status)








