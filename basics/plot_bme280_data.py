
from datetime import datetime
import numpy as np
import time

now = datetime.now()

# tempo = datetime.strptime('09:13:37','%H:%M:%S')

conv_date = lambda x: datetime.strptime(x,"%Y-%m-%d")
conv_temp = lambda x: x
conv_str = lambda x: x

def conv_time(x):
    if '.' in x:
        t = datetime.strptime(x,'%H:%M:%S.%f')
        # print t
    else:
        t = datetime.strptime(x,'%H:%M:%S')
    return t
        
f = open('data.log')

# Struttura d_t_temp:
# data tempo pressione umidita_relativa temperatura
d_t_temp =  np.genfromtxt(f, delimiter=" ", converters={0: conv_date,1: conv_time,2: conv_temp, 3: conv_str, 4: conv_temp, 5: conv_str, 6:conv_temp, 7: conv_str})
print "data tempo pressione umidita_relativa temperatura"
print d_t_temp
f.close()


data_temp = []
to_plot = np.zeros( (len(d_t_temp),5) )
# print to_plot.shape
for i,f in enumerate(d_t_temp):
    data_temp.append([datetime.combine(datetime.date(f[0]), datetime.time(f[1])), f[2], f[4], f[6]])
    #to_plot[i,0] =  datetime.strftime(data_temp[-1][0],'%f')
    to_plot[i,0] =  time.mktime(data_temp[-1][0].timetuple())
    print now-data_temp[-1][0]
    # to_plot[i,0] =  data_temp[-1][0]
    to_plot[i,1] =  data_temp[-1][1]
    to_plot[i,2] =  data_temp[-1][2]
    to_plot[i,3] =  data_temp[-1][3]


to_plot = np.array(to_plot)
# print to_plot
# print datetime.strftime(data_temp[0][0],'%f')

# Grafici
import matplotlib.pyplot as plt
#from matplotlib import pylab

f, axarr = plt.subplots(3, sharex=True)
f.patch.set_facecolor('black')
for ax in axarr:
    ax.set_axis_bgcolor('black')
    for pos in ['top','bottom','left','right']:
        ax.spines[pos].set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_color('white')
    ax.title.set_color('white')
    
axarr[0].plot(to_plot[:,0], to_plot[:,1],'w')
axarr[0].set_title('Pressione atmosferica')
axarr[0].set_ylabel('Pressione (Pa)')

axarr[1].set_title('Umidita relativa')
axarr[1].set_ylabel('Umidita relativa (%)')
axarr[1].plot(to_plot[:,0], to_plot[:,2],'w')

axarr[0].set_title('Temperatura')
axarr[0].set_ylabel('Temperatura (C)')
axarr[2].plot(to_plot[:,0], to_plot[:,2],'w')
axarr[2].set_xlabel('Tempo in ms dal 1 Gen 1900')
# pto_plot[:,0], to_plot[:,1]ylab.plot(to_plot[:,0], to_plot[:,1])
#pylab.plot( to_plot[:,0])

MagicMirror_dir = '/home/ipsia/git/MagicMirror/modules/default/newsfeed/'
file_to_save = MagicMirror_dir + 'foto.png'

plt.savefig(file_to_save,
            dpi=None,
            facecolor='k',
            edgecolor='w',
            orientation='portrait',
            papertype=None,
            format=None,
            transparent=False,
            bbox_inches=None,
            pad_inches=0.1,
            frameon=None
            )


plt.show()
