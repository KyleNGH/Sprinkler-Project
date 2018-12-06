'''
sensor_main.py
Main Program for Remote Sensor
Kyle GH
December 2018
EE496 


'''

### Import Libraries
from sensor_input import *
from time import sleep


### main program to constantly run
while True:
    
    data = sensor_data()

    send_data(data)
    weather = get_weather()

    #weather ,soil
    append_save_data_file(weather,data)

    sleep(5)

#add_data_to_file()

#data = 

print('END TRANSMISSION')




