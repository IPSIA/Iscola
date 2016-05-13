
from datetime import datetime
import numpy as np
import time

data = datetime.strptime("07-05-2016","%d-%m-%Y")

tempo = datetime.strptime('09:13:37','%H:%M:%S')

conv_date = lambda x: datetime.strptime(x,"%Y-%m-%d")
conv_temp = lambda x: x 
def conv_time(x):
    if '.' in x:
        t = datetime.strptime(x,'%H:%M:%S.%f')
        # print t
    else:
        t = datetime.strptime(x,'%H:%M:%S')
    return t
        
f = open('dati11maggio.txt')
d_t_temp =  np.genfromtxt(f, delimiter=" ", converters={0: conv_date,1: conv_time,2: conv_temp,3: conv_temp})
# print d_t_temp
f.close()
data_temp = []
to_plot = np.zeros( (len(d_t_temp),3) )
print to_plot.shape
for i,f in enumerate(d_t_temp):
    data_temp.append([datetime.combine(datetime.date(f[0]), datetime.time(f[1])), f[2], f[3]])
    #to_plot[i,0] =  datetime.strftime(data_temp[-1][0],'%f')
    to_plot[i,0] =  time.mktime(data_temp[-1][0].timetuple())
    to_plot[i,1] =  data_temp[-1][1]
    to_plot[i,2] =  data_temp[-1][2]

to_plot = np.array(to_plot)
print datetime.strftime(data_temp[0][0],'%f')

# Grafici
import matplotlib.pyplot as plt
#from matplotlib import pylab

f, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(to_plot[:,0], to_plot[:,1])
axarr[0].set_title('Temperature')
axarr[1].set_xlabel('Tempo in ms dal 1 Gen 1900')
axarr[0].set_ylabel('Temperatura (C)')
axarr[1].set_ylabel('Umidita (digital value)')
axarr[1].plot(to_plot[:,0], to_plot[:,2])
# pto_plot[:,0], to_plot[:,1]ylab.plot(to_plot[:,0], to_plot[:,1])
#pylab.plot( to_plot[:,0])
 
plt.savefig('Temp_plot.png', dpi=None, facecolor='k', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None)


plt.show()
