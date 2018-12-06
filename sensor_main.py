'''
sensor_main.py
Main Program for Remote Sensor
Kyle GH
December 2018
EE496 


'''

### Import Libraries
from sensor_input import *
from gpiozero import CPUTemperature
from time import sleep, time

### main program to constantly run
while True:
    
    data = sensor_data()

    
    weather = get_weather()


    #weather ,soil
    append_save_data_file(weather,data)
    
    
    
    send_data(data)

    #graph(data)

    sleep(1)

#add_data_to_file()

#data = 

print('END TRANSMISSION')




