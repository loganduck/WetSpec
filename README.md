# WetSpec
WetSpec can be used to monitor changing weather conditions in remote environments.

## Hardware
* [Raspberry Pi 3 B+](https://www.seeedstudio.com/GrovePi-Starter-Kit-for-Raspberry-Pi-A-B-B-2-3-CE-certified.html)
* [GrovePi+ Starter Kit](https://www.seeedstudio.com/GrovePi-Starter-Kit-for-Raspberry-Pi-A-B-B-2-3-CE-certified.html)

### Parts used from GrovePi kit:
* GrovePi+
* Temp&Humi Sensor (DHT)
* Green LED
* Blue LED
* Red LED
* Light Sensor
* Cables (5)

### Additional :
* Monitor with HDMI input
* HDMI cable
* 2.5A micro USB power supply
* USB keyboard and mouse
* Micro SD card with [N00BS](https://www.raspberrypi.org/documentation/installation/noobs.md) installed

## Specifications
### Light Sensor:
Temperature and humidity is only monitored during daytime hours and daytime conditions; sensor readings must not be recorded outside these times or conditions, or there might risk skewing the data the platform collects.

### Frequency of Data:
During operating hours, readings must be taken once every 30 minutes, and the readings must be incrementally stored in a JSON file. To clarify, each reading must be added to a single JSON file so that a flat file of readings is stored over time.

### Output Visual Using LEDs:
* Green LED lights up when the last conditions are: **temperature > 60 and < 85, and humidity is < 80%**
* Blue LED lights up when the last conditions are: **temperature > 85 and < 95, and humidity is < 80%**
* Red LED lights up when the last conditions are: **temperature > 95**
* Green and Blue LED light up when the last conditions are: **humidity > 80%**

Data will be stored in `weather.json` and can be **reset** by editing the file as such:
```
{"weather":[]}
```

## Installation  
From the Raspberry Pi Terminal:

1. **Update** your system's package list using:
`sudo apt update`
2. **Upgrade** all your installed packages to their latest versions with: 
`sudo apt full-upgrade`

Specific modifications must be made to successfully operate the GrovePi.

It is important to carefully follow this [tutorial](https://www.dexterindustries.com/grovepi-tutorials-documentation/) to configure software and updating firmware so the RPi can successfully communicate with the Grove.

##Running the program 
1. Connect the Grove to RPi
2. Add sensors to the following ports:  
Light Sensor = 0  
Temp&Hum Sensor (DHT) = 7  
Green LED = 2  
Blue LED = 3  
Red LED = 4  
3. Connect USB keyboard and mouse to RPi.  
4. Connect one end to HDMI to RPi and other to monitor.  
5. Connect power supply to Raspberry Pi and power on
6. Install this project in `Dexter/GrovePi/Software/Python` and run `WetSpec.py`.
7. There should be no errors if everything was followed in the [tutorial](https://www.dexterindustries.com/grovepi-tutorials-documentation/) above. As long as it is daytime, let the system run for a a few hours.
8. End the program and open `dashboard.html` from the project folder and the dashboard can be viewed.

### Example of dashboard:
![Dashboard](/dashboard.png)
