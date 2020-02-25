#!/usr/bin/env python
import grovepi
import json
import time
import math
import datetime

# defining port allocations
light_sensor = 0
dht_sensor = 7
led_green = 2
led_blue = 3
led_red = 4

threshold = 10

grovepi.pinMode(light_sensor,"INPUT")
grovepi.pinMode(led_green,"OUTPUT")
grovepi.pinMode(led_blue,"OUTPUT")
grovepi.pinMode(led_red,"OUTPUT")

# writes data to 'weather.json'.
def write_json(data, filename='weather.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# updated the statuses of LEDs.
def update_led(g_val, b_val, r_val):
    grovepi.digitalWrite(led_green, g_val)
    grovepi.digitalWrite(led_blue, b_val)
    grovepi.digitalWrite(led_red, r_val)

#initialize LEDs off
update_led(0,0,0)

while True:
    with open('weather.json') as weather:
        try:
            readings = json.load(weather)
            [temperature, humidity] = grovepi.dht(dht_sensor, 0) #0=blue chip
            light_sensor_value = grovepi.analogRead(light_sensor)
            
            # hh and mm represent hour and minute, respectively. This will be used to print current state with time to the console. 
            hh = datetime.datetime.now().hour
            mm = datetime.datetime.now().minute
                    
            # calculate resistance of sensor in K
            resistance = (float)(1023 - light_sensor_value) * 10 / light_sensor_value
            if math.isnan(temperature) == False and math.isnan(humidity) == False:
                
                '''
                Temperature and humidity will only be monitored during daytime hours and conditions. When the resistance
                value is less than threshold, it is represented as daytime.
                '''
                if resistance < threshold: # daytime
                    data = readings['weather']
                    
                    # convert to fahrenheit
                    temperature = int((temperature * (9/5)) + 32 )
                    humidity = int(humidity)
                    
                    values = {"temperature": temperature, "humidity": humidity}
                    print('{}:{} || t: {}, h: {}, led: {} || light: {}'.format(hh, mm, temperature, threshold, values, light_sensor_value))
                    data.append(values)
                    write_json(readings)
                   
                    if temperature > 60 and temperature < 85 and humidity < 80:
                        update_led(1,0,0)
                    elif temperature > 85 and temperature < 95 and humidity < 80:
                        update_led(0,1,0)
                    elif temperature > 95:
                        update_led(0,0,1)
                    elif humidity > 80:
                        update_led(1,1,0)
                else: # nighttime
                    print('{}:{} || no data, too dark'.format(hh, mm))
                    update_led(0,0,0)
                # calculate readings every 30 minutes
                time.sleep(30*60)
        except IOError:
            print('error')