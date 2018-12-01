#   File: Sensor Input
#   Purpose: Take data from sensor and save to file
#   Author: Kyle GH
#   Date: Nov 11, 2018

### import libraries







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



###### To save file on csv
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
            
###### Get data from sensor  
def sensor_data():
    # Analog Input using MCP3008 Chip
    from gpiozero import MCP3008
    from gpiozero import PWMLED
    from time import sleep

    #	pot = variable resistor
    #	Top Left corner 	= 0.0	,zero
    #	Bottom Left corner 	= 1.0	,max
    #	find voltage by multiplying max possible, 3.3v
    #  	voltage = vref * pot.value

    voltage = [0,0,0,0,0,0,0,0]
    vref = 3.3

    led = PWMLED(21)
    led2= PWMLED(20)
    pot = MCP3008(0)


    led.on()	# led lit
    led2.source = pot.values
    print(pot.value)
    sleep(5)
    led.off()
    led2.close()

### use api key to grab weather data
def get_weather():
    import pyowm

    # api key
    owm = pyowm.OWM("b508f902bfd4f9d38491e1b8557c675f")

    observation = owm.weather_at_place("Honolulu,us")

    w = observation.get_weather()

    print(w)

### get sensor data and weather data and add to file
#def add_data_to_file

    
### main program to constantly run
#while True:
    
data = sensor_data()

get_weather()

create_save_data_file()

#add_data_to_file()

#data = 







