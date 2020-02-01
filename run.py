__author__ = "Jakob Aungiers"
__copyright__ = "Jakob Aungiers 2018"
__version__ = "2.0.0"
__license__ = "MIT"

import os
import json
import time
import math
import matplotlib.pyplot as plt
import serial
import numpy as np

from core.data_processor import DataLoader
from core.model import Model

fig = plt.figure(facecolor='white')

def plot_results(predicted_data, true_data):
    plt.cla() #clear previous fig
    ax = fig.add_subplot(111)
    ax.plot(true_data, label='True Data')
    plt.plot(predicted_data, label='Prediction')
    plt.legend()



def plot_results_multiple(predicted_data, true_data, prediction_len):
    fig = plt.figure(facecolor='white')
    ax = fig.add_subplot(111)
    ax.plot(true_data, label='True Data')
	# Pad the list of predictions to shift it in the graph to it's correct start
    for i, data in enumerate(predicted_data):
        padding = [None for p in range(i * prediction_len)]
        plt.plot(padding + data, label='Prediction')
        plt.legend()
    plt.show()


def main():
    
    configs = json.load(open('config.json', 'r'))
    if not os.path.exists(configs['model']['save_dir']): os.makedirs(configs['model']['save_dir'])

    model = Model()
    model.build_model(configs)

    #get live sensor data from Arduino and predict next 10 sensor data
    sensor_port = serial.Serial('COM7', 9600)
    sensor_port.close()
    sensor_port.open()
    seq_len=configs['data']['sequence_length'],
    sensor_data= []
    predictions_data = []
    live_data = np.arange(seq_len[0]-1) 
    
    plt.ion() #real time graph

    while True:
        i=0
        while i < seq_len[0]-1:              # store incoming data to testing data array
            b = sensor_port.readline()         # read a byte string
            live_data[i]= float(b.decode())
            sensor_data.append(live_data[i])
            i+=1    
        sensor_struct_data = live_data[np.newaxis,:,np.newaxis] #contruct live data for LSTM
        plot_results(predictions_data[-150:],sensor_data[-100:])
        plt.show()
        plt.pause(0.1) #critical to display continous img

        #predict every 10 seq_len
        if len(sensor_data) > 5 * seq_len[0]:
            predictions= model.predict_sequence_live(sensor_struct_data, configs['data']['sequence_length']) #Shift the window by 1 new prediction each time, re-run predictions on new window
            predictions_data.append(predictions)

        #train every 100 seq_len
        if len(sensor_data) >30 * seq_len[0]:
            np.savetxt('data\sensor.csv', sensor_data, delimiter = ',', header='sensor_value')

        #load data for training
            data = DataLoader(
            os.path.join('data', configs['data']['filename']),
            configs['data']['train_test_split'],
            configs['data']['columns']
            )

            x, y = data.get_train_data(
                seq_len=configs['data']['sequence_length'],
                normalise=configs['data']['normalise']
                )
        # in-memory training
            model.train(
                x,
                y,
                epochs = configs['training']['epochs'],
                batch_size = configs['training']['batch_size'],
                save_dir = configs['model']['save_dir']
            )
            sensor_data =sensor_data[-100:]


if __name__ == '__main__':
    main()




    ''' code warehouse
    # out-of memory generative training
    steps_per_epoch = math.ceil((data.len_train - configs['data']['sequence_length']) / configs['training']['batch_size'])
    model.train_generator(
        data_gen=data.generate_train_batch(
            seq_len=configs['data']['sequence_length'],
            batch_size=configs['training']['batch_size'],
            normalise=configs['data']['normalise']
        ),
        epochs=configs['training']['epochs'],
        batch_size=configs['training']['batch_size'],
        steps_per_epoch=steps_per_epoch,
        save_dir=configs['model']['save_dir']
    )


        x_test, y_test = data.get_test_data(
        seq_len=configs['data']['sequence_length'],
        normalise=configs['data']['normalise']
        )
    
    '''

        #other prediction mode
    #predictions = model.predict_point_by_point(x_test)
    #predictions = model.predict_sequence_full(sensor_data, configs['data']['sequence_length']) #Shift the window by 1 new prediction each time, re-run predictions on new window
    #predictions2 = model.predict_sequences_multiple(x_test, configs['data']['sequence_length'], configs['data']['sequence_length'])
    #plot_results_multiple(predictions2, y_test, configs['data']['sequence_length'])
  