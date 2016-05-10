
from datetime import datetime
import numpy as np

data = datetime.strptime("07-05-2016","%d-%m-%Y")

tempo = datetime.strptime('09:13:37','%H:%M:%S')

conv_date = lambda x: datetime.strptime(x,"%d-%m-%Y")
conv_temp = lambda x: x 
def conv_time(x):
    if '.' in x:
        t = datetime.strptime(x,'%H:%M:%S.%f')
        # print t
    else:
        t = datetime.strptime(x,'%H:%M:%S')
    return t
        
f = open('Temp_dati.dat')
d_t_temp =  np.genfromtxt(f, delimiter=" ", converters={0: conv_date,1: conv_time,2: conv_temp})
# print d_t_temp
f.close()
data_temp = []
to_plot = np.zeros( (len(d_t_temp),2) )
print to_plot.shape
for i,f in enumerate(d_t_temp):
    data_temp.append([datetime.combine(datetime.date(f[0]), datetime.time(f[1])), f[2]])
    to_plot[i,0] =  datetime.strftime(data_temp[-1][0],'%f')
    to_plot[i,1] =  data_temp[-1][1]


to_plot = np.array(to_plot)
print datetime.strftime(data_temp[0][0],'%f')

# Grafici
from matplotlib import pylab

f = pylab.figure()
pylab.plot(to_plot[:,0], to_plot[:,1])
pylab.xlabel('Tempo in ms dal 1 Gen 1900')
pylab.ylabel('Temperatura (C)')
pylab.show()
