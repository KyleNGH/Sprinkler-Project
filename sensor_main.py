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
from time import sleep
import matplotlib.pyplot as plt


plt.ion()
x1 = []
x2 = []
y1 = [] 

### main program to constantly run
while True:
    
    data = sensor_data()

    
    weather = get_weather()


    #weather ,soil
    append_save_data_file(weather,data)
    
    graph(data)
    
    send_data(data)

    sleep(1)

#add_data_to_file()

#data = 

print('END TRANSMISSION')




