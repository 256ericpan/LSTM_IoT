# LSTM for live IoT data prediction

## Introduction
LSTM_IoT is an project using machine learning (LSTM) to predict over live IoT sensor data 

For data scientist, to fetch real world data and user machine learning to find out "interesting" data. 
For ai resercher, to get more data to tweak LSTM machines or pipe the example to more advanced machine learning setup. 
For the rest of us, monitor some parameter (temperature, sound, humidity, lightness, movement, air pressor, color, rotation, particle count, gas, PH ...) on physical things through sensors, predict its trend and detect abnormity. 

The project is largely inspired and based on depending on https://github.com/jaungiers/LSTM-Neural-Network-for-Time-Series-Prediction and http://wiki.seeedstudio.com/Grove_Beginner_Kit_for_Arduino/ 

![anim_sound3.gif](https://raw.githubusercontent.com/256ericpan/img.bed/master/image/anim_sound3.gif)

## requirement

### software
Install requirements.txt file to make sure correct versions of libraries are being used.

* Python 3.5.x
* TensorFlow 1.10.0
* Numpy 1.15.0
* Keras 2.2.2
* pyserial 
* Matplotlib 2.2.2
* Arduino IDE 

### hardware 

* a host PC/server running Python3 
* an Arduino compatible board like Seeeduino
* some Grove sensors http://wiki.seeedstudio.com/Sensor/ 

![20200202213147.png](https://raw.githubusercontent.com/256ericpan/img.bed/master/image/20200202213147.png)

## installation

### Arduino
select right serial port, remember the **port number**(like COM7) to change host settings later. 
change 

![20200202212706.png](https://raw.githubusercontent.com/256ericpan/img.bed/master/image/20200202212706.png)

select the right pin target sensor is using. For grove modules, find the first silkscreen near connected Grove connctor.
```c
    sensorPin = A0;  // set the pin to target sensor
```
open serial plot to validate the sensor data is alive
![serial plotter pic]

### Python
maker sure all the environment are prepared, exactly as the ver. Anaconda is recommended to create a dedicated version. 

setup the serial port to Seeeduino
```python
    sensor_port = serial.Serial('COM7', 9600)
```

## Run
Yes, run.py will
1. gather all the libraries  
2. load the configuration in config.json (important to tweak LSTM to fit your situation)
3. Build the Neuron Network model
4. setup serial port and other variables
5. loop every 0.1 second
   1. fetch a group of sensor data 
   2. plot for the live sensor data after a group of data
   3. every 0.5 seconds: predict with latest data 
   4. every 10 seconds: train LSTM again with latest data
   5. Trim the sensor data to latest 100 

Watch how prediction evolves over time. 
Try change the sensing objects and see how the LSTM neuron network adapt the new trend. 

## some results 
### Light
Sensing with [Grove Light sensor](http://wiki.seeedstudio.com/Grove-Light_Sensor/): change the lightness around sensor to see the live data change. Prediction can't forecast sudden human interfernece (yet), but will catch up and predict following stablized situations. 

![anim_sound3.gif](https://raw.githubusercontent.com/256ericpan/img.bed/master/image/anim_sound3.gif)


### Sound
Sensing with [Grove Sound sensor](http://wiki.seeedstudio.com/Grove-Sound_Sensor/): since raw loudness is more verstile without obivous patterns, LSTM is predicting the baseline increase as moving closer to speaker and ignored the peaks. 

![sound_start.png](https://raw.githubusercontent.com/256ericpan/img.bed/master/image/sound_start.png)

## To do :
### detect abnormity 
### More static data like temperature
### Tune the LSTM neuron network
### User multiple sensor and buttons to lable data 
### Deploy on edge computing 

## Thanks
to Jakob Aungiers, Altum Intelligence ltd 
https://github.com/jaungiers/LSTM-Neural-Network-for-Time-Series-Prediction

With his code, An initial offline testing (as below) was done with actual stored sensor data was quick convincing, thus I'm confident in accomplish this project.

![Figure_sound.png](https://raw.githubusercontent.com/256ericpan/img.bed/master/image/Figure_sound.png)

## More about LSTM
![20200202203217.png](https://raw.githubusercontent.com/256ericpan/img.bed/master/image/20200202203217.png) 
https://pathmind.com/wiki/lstm


