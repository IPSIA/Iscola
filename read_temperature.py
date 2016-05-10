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
for f in d_t_temp:
    data_temp.append([datetime.combine(datetime.date(f[0]), datetime.time(f[1])), f[2]])

#print data_temp
