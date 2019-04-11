# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 10:23:25 2018

@author: cerecam
"""
import numpy as np
import matplotlib.pyplot as plt

def getresults(name, influx_file, efflux_file, key):
    filename = '/home/etg/Desktop/' + key + '/Flux_results'+name+'.inp'
    fread = open(filename, 'r')
    lines = fread.readlines()
    fread.close()
    for x in range(0, len(lines), 2):
        # total_int_file.append(float(lines[x+3].split(':')[1]))
        influx_file.append(float(lines[x].split(':')[1]))
        efflux_file.append(float(lines[x+1].split(':')[1]))
    return influx_file, efflux_file

colors = {'25PER' : 'b','34PER' : 'r','42PER' : 'g','50PER' : 'k'}
## 34 PER every 2 inc
## 50 PER every 3 inc
# filenames = ['S1_34PER', 'S2_34PER', 'S3_34PER']
filenames = {'25PER': ['S1_25PER_new3', 'S2_25PER_new3', 'S3_25PER_new3', 'S4_25PER_new3', 'S5_25PER_new3'],
             '42PER': ['S1_42PER_new2', 'S2_42PER_new3'],
             '34PER': ['S1_34PER_new2', 'S2_34PER_new2'],
             '50PER':['S1_50PER_new3', 'S2_50PER_new3']}
areaPerEle = (96.0/100.0)*(96.0/100.0)
areas = {'25PER': [7148*areaPerEle, 6961*areaPerEle], '34PER': [6403*areaPerEle,6109*areaPerEle],
         '42PER': [5748*areaPerEle,5382*areaPerEle], '50PER': [5056*areaPerEle,4682*areaPerEle]} # in = Z1, out = Z0
# filenames = ['S1_50PER', 'S2_50PER', 'S3_50PER']
# filenames = ['S1_34PER']
plt.figure(figsize=(17, 10))
m = 0
for key, values in filenames.items():
    influx = []
    efflux = []
    for fname in values:
        # Get data from Check_results'jobname'.inp files
        influx, efflux = getresults(fname, influx, efflux, key)

        # influxTotal.extend(influx)
        # effluxTotal.extend(efflux)

    # Calcuate increment that the concentration limit was first reached
    #limit = [efflux.index(y) for y in efflux if y < 589][0]

    # Normalize values for visualisation for trend
    # total_int_norm = [i/max(total_int, key=abs) for i in total_int]
    # influx_norm = [i/max(influx, key=abs) for i in influx]
    # efflux_norm = [i/max(efflux, key=abs) for i in efflux]
    avgCorrectionFactorIn = 8208.55/areas[key][0]
    avgCorrectionFactorOut = 8066.41/areas[key][1]
    print(key)
    print(avgCorrectionFactorOut)
    print(avgCorrectionFactorIn)
    influx_norm = [i*avgCorrectionFactorIn for i in influx]
    # efflux_norm = efflux
    efflux_norm = [(i/-1.0)*avgCorrectionFactorOut for i in efflux]
    # t_end = len(influx_norm)/2.0*3.0
    # time = np.linspace(0, t_end, len(influx_norm))
    if key =='34PER':
        t_end = len(influx_norm) / 2.0 * 5.0
        time = np.linspace(0, t_end, len(influx_norm))
    elif key == '25PER':
        t_end = len(influx_norm) / 2.0 * 3.0
        time = np.linspace(0, t_end, len(influx_norm))
    elif key == '42PER' :
        t_end = len(influx_norm)/2.0*3.0
        time = np.linspace(0, t_end, len(influx_norm))
    elif key == '50PER':
        t_end = len(influx_norm)/2.0*3.0
        time = np.linspace(0, t_end, len(influx_norm))

    # time = np.linspace(0, len(influx_norm), len(influx_norm))

    # Lines fo best fit
    # line_influx = np.poly1d(np.polyfit(time, influx_norm, 4))
    # line_total_int = np.poly1d(np.polyfit(time, total_int_norm, 3))

    #Plot figures
    plt.plot(time, influx_norm, color = colors[key], label = key + ': influx')
    # plt.plot(time, efflux_norm, lineStyle=':',color = colors[key], label = key + ': efflux')
    #         time, line_influx(time), 'b--',
    #         time, line_total_int(time), 'r--')
    # plt.plot([limit]*2,[min(min(total_int_norm),min(influx_norm),min(efflux_norm))-0.1,1.1],'k')
    # plt.plot([time[0], time[-1]], [1.0, 1.0], 'k')
    m += 1
plt.xticks(np.arange(0, max(time), step=100))
plt.legend(loc='best')
plt.ylim(bottom=0.0)
plt.grid(b=True, which='minor')
plt.show()
