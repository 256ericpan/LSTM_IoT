import serial
import time
import numpy
import matplotlib.pyplot as plt

# set up the serial line
ser = serial.Serial('COM7', 9600)
time.sleep(2)
# Read and record the data
data =[]                       # empty list to store the data
for i in range(1000):
    b = ser.readline()         # read a byte string
    string_n = b.decode()  # decode byte string into Unicode  
    string = string_n.rstrip() # remove \n and \r
    flt = float(string)        # convert string to float
    print(flt,i)
    data.append(flt)           # add to the end of data list
    time.sleep(0.01)            # wait (sleep) 0.1 seconds

ser.close()

#save data to csv
numpy.savetxt('data\sensor.csv', data, delimiter = ',', header='sensor_value')


# show the data
# for line in data:
#   print(line)

# plot the actual data
plt.plot(data)
plt.xlabel('Time (seconds)')
plt.ylabel('Sensor Reading')
plt.title('Sensor Reading vs. Time (10ms)')
plt.show()