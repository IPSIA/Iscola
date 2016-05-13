#!/usr/bin/python
# get lines of text from serial port, save them to a file

 
from __future__ import print_function
import serial, io, datetime

addr  = '/dev/ttyUSB0'  # serial port to read data from
baud  = 9600            # baud rate for serial port
fname = 'dati11maggio.txt'   # log file to save data in
fmode = 'a'             # log file mode = append

with serial.Serial(addr,baud) as pt, open(fname,fmode) as outf:
    spb = io.TextIOWrapper(io.BufferedRWPair(pt,pt,1),
        encoding='ascii', errors='ignore', line_buffering=True)
    spb.readline()  # throw away first line; likely to start mid-sentence (incomplete)
    while (1):
	data = str(datetime.datetime.now())
        x = str(spb.readline()) # read one line of text from serial port
        meteo = data + ' ' + x
	print (meteo,end='')    # echo line of text on-screen
        outf.write(meteo)       # write line of text to file
        outf.flush()        # make sure it actually gets written out
                                      
                                      