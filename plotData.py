#plotData.py

""" This program will read in a data file from Gnu Radio and plot it.

    Ellie White 25 Feb. 2017

"""

import pylab as plt
import os
import numpy as np

def main(fftsize=8192):

    infile = input("Enter the name of the file to read >>> ")
    srate = int(input("What is the sampling rate of your SDR? >>> "))
    #freq = float(input("What frequency do you want to look at? >>> "))
    tothours = int(input("How long did you record (in hours)? >>> "))
    data = []

    size = os.path.getsize(infile) / 4
    shape = (size/fftsize, fftsize)
    x = np.memmap(infile, dtype='float32', mode = 'r', shape=shape)
       
    idx = np.linspace(0, tothours, len(x))

    #chanwid = srate/fftsize
    #chan =(freq + 2586.47)
    
    sigchans = [4214]
    ts = []
    nchan = 4250
    noisechan = []
    
    for i in range(20):
        noisechan.append(nchan)
        nchan += 1
            
    for i in x:
        
        cvalues = []
        svalues = []
        
        for c in noisechan:
            cvalue = i[c]
            cvalues.append(cvalue)
        for s in sigchans:
            svalue = i[s]
            svalues.append(svalue)
            
        avgn = np.mean(cvalues)
        avgs = np.mean(svalues)
        ts.append((avgs-avgn))   #appends each time sample from this channel
        
    freqPlot = np.mean(x, axis=0)
    fmin = 2586.47-(srate/2)
    fmax = 2586.47+(srate/2)
    fidx = np.linspace(fmin, fmax, len(freqPlot))

    #plt.plot(fidx, freqPlot)
    plt.plot(freqPlot)
    plt.show()

    plt.plot(idx, ts)
    plt.show()

    print(len(x))
    print(len(x[0]))

if __name__ == "__main__":
    main()
