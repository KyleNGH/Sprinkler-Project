#   File: Sensor Input
#   Purpose: Take data from sensor and save to file
#   Author: Kyle GH
#   Date: Nov 11, 2018

### import libraries
from bluetooth import *







######### Definitions

# get current date or time
# type [  getdatetime('TYPE') replace type with desired output using ' or "

def getdatetime(timedateformat='complete'):
    from datetime import datetime
    timedateformat=timedateformat.lower()

    if timedateformat == 'day':
        return (( str(datetime.now() )).split(' ')[0]).split('-')[2]
    elif timedateformat == 'month':
        return (( str(datetime.now() )).split(' ')[0]).split('-')[1]
    elif timedateformat == 'year':
        return (( str(datetime.now() )).split(' ')[0]).split('-')[0]
    elif timedateformat == 'hour':
        return ((( str(datetime.now() )).split(' ')[1]).split('.')[0]).split(':')[0]
    elif timedateformat == 'minute':
        return ((( str(datetime.now() )).split(' ')[1]).split('.')[0]).split(':')[1]
    elif timedateformat == 'second':
        return ((( str(datetime.now() )).split(' ')[1]).split('.')[0]).split(':')[2]
    elif timedateformat == 'yearmonthday':
        return ( str(datetime.now() )).split(' ')[0]
    elif timedateformat == 'daymonthyear':
        return (( str(datetime.now() )).split(' ')[0]).split('-')[2]+'-'+\
                ((str(datetime.now() )).split(' ')[0]).split('-')[1]+'-'+\
                ((str(datetime.now() )).split(' ')[0]).split('-')[0]
    elif timedateformat == 'hourminutesecond':
        return (( str(datetime.now() )).split(' ')[1]).split('.')[0]
    elif timedateformat == 'secondminutehour':
        return ((( str(datetime.now() )).split(' ')[1]).split('.')[0]).split(':')[2]+':'+\
                ((( str(datetime.now() )).split(' ')[1]).split('.')[0]).split(':')[1]+':'+\
                 ((( str(datetime.now() )).split(' ')[1]).split('.')[0]).split(':')[0]
    elif timedateformat == 'complete':
        return str(datetime.now() )
    elif timedateformat == 'datetime':
        return ( str(datetime.now() )).split('.')[0]
    elif timedateformat == 'timedate':
        return (( str(datetime.now() )).split('.')[0]).split(' ')[1]+' '+\
                ((str(datetime.now() )).split('.')[0]).split(' ')[0]                




###### To create csv file for saved data
#   mode - open( name, mode('r'eading or 'w'riting or 'a'ppending)
def create_save_data_file():
    date = getdatetime('yearmonthday')

    output_file = 'data_{0}.csv'.format( date )
    
    try:
        with open(output_file,'r') as f:
            print(output_file + ' exists.')
            
    except:    
        with open(output_file,'w') as f:
            header = ["date","hour","minute","temp","weather","soil"]
            f.write(','.join(header)+'\n')
            print(output_file + ' was created.')
    finally:
        f.close()
            

###### To save file on csv
#   mode - open( name, mode('r'eading or 'w'riting or 'a'ppending)
def append_save_data_file(weather,soil):
    from gpiozero import CPUTemperature
    import os
    
    date = getdatetime('yearmonthday')
    day = getdatetime('day')
    hour = getdatetime('hour')
    min  = getdatetime('minute')
    sec = getdatetime('second')
    currently = getdatetime('hourminutesecond')
    temp = CPUTemperature().temperature


    output_file = 'data_{0}.csv'.format( date )
    
    try:
        with open(output_file,'r') as f:
            print(output_file + ' file exists.')
            
    except:    
        with open(output_file,'w') as f:
            header = ["Day","Hour","Minute","Second","Temperature","Weather","Soil"]
            f.write(','.join(header)+'\n')
            print(output_file + ' file was created.')
    finally:
        with open(output_file,'a') as f:
            line = [day,hour,min,sec,temp,weather,soil]
            next_line = [ str(line) for items in line ]
            f.write(','.join( next_line )+'\n')
            print(currently + ' data added to ' + output_file )
        
        f.close()

### graph dat
def graph( data ):
    # interactive plots
    y1.append(data)
    x1.append(time())
    #x2.append(temp)
    
    plt.clf()
    plt.scatter( x1,y )
    plt.plot( x1,y )
    plt.draw()

###### Get data from sensor  
def sensor_data():
    # Analog Input using MCP3008 Chip
    from gpiozero import MCP3008
    from gpiozero import PWMLED
    from time import sleep


    #   pot = variable resistor
    #   Top Left corner     = 0.0   ,zero
    #   Bottom Left corner  = 1.0   ,max
    #   find voltage by multiplying max possible, 3.3v
    #   voltage = vref * pot.value

    voltage = [0,0,0,0,0,0,0,0]
    vref = 3.3

    led = PWMLED(21)
    led2= PWMLED(20)
    pot = MCP3008(0)


    led.on()    # led lit
    led2.source = pot.values
    value = pot.value
    sleep(5)
    led.off()
    led2.close()
    
    print("Sensor Data Read")
    
    return value
    
### use api key to grab weather data
def get_weather():
    import pyowm

    # api key
    owm = pyowm.OWM("b508f902bfd4f9d38491e1b8557c675f")

    observation = owm.weather_at_place("Honolulu,us")

    w = observation.get_weather()

    print("Weather Received")
    
    return w
    
### get sensor data and weather data and add to file
#def add_data_to_file

### bluetooth data reciever
# server recieves data from client
# rfcomm_server.py
#receive

def receive_data():

    server_socket = BluetoothSocket( RFCOMM )

    server_socket.bind(("",1))
    server_socket.listen(1)


    client_socket,address = server_socket.accept()
    data = client_socket.recv(1024)

#   print("received [%s]" % data)
    print("Transmission success")
    client_socket.close()
    server_socket.close()
    
    return data

### bluetooth data sender
#Sensor client send data to server
# sudo rfcomm help

def send_data(data):
    from time import sleep
    


    package = str(data)
    while True:
        try:
                #create client socket
            client_socket=BluetoothSocket( RFCOMM )
            addr = "B8:27:EB:DF:04:DF"
            port = 1
            client_socket.connect((addr,port))
    
            client_socket.send( package )

            print("Data Sent")

            client_socket.close()
            break
        except:
            print('Waiting for Connection')
            sleep(10)
       

'''

## Import Libraries
from sensor_input import *


### main program to constantly run
#while True:
    
data = sensor_data()

send_data(data)
get_weather()

create_save_data_file()

#add_data_to_file()

#data = 

print ("END TRANSMISSION")
'''



