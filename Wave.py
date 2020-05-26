from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LinearSegmentedColormap
from matplotlib import cm
import matplotlib.pyplot as plt
import math
import numpy as np
import glob
from PIL import Image


#Путь до картинок и до GIF
fp_in = "frames\step*.png"
fp_out = "image.gif"

#Параметры
par_l = 1/2
par_t = 100

#По умолчанию
x_r = np.arange(-1, 1, 0.006)
y_r = np.arange(-1, 1, 0.006)
        
xgrid, ygrid = np.meshgrid(x_r, y_r)
dataX_0 = xgrid-xgrid
dataY_0 = xgrid-xgrid
        
#Создание источника(координаты x и y, длина волны и период)
#E(r, t)=E_0*cos(k*r + w*t + phi_0)
def source(x, y, l, t, phi):
    global xgrid
    global ygrid
    x_g = xgrid-x
    y_g = ygrid-y
    
    r = np.sqrt(x_g*x_g + y_g*y_g)
    data = np.cos(-r*2*math.pi/l + 2*math.pi/t*i + phi)
    data_x = x_g/r*data
    data_y = y_g/r*data
    global dataX_0
    global dataY_0
    dataX_0 = dataX_0+data_x
    dataY_0 = dataY_0+data_y

# отдельная функция, в которой задаются x, y, z
def makeData(i):
        source(0.5, 0, par_l, par_t, 0)
        source(-0.5, 0, par_l, par_t, 0)
        
        #zgrid = np.sin(np.sqrt(xgrid*xgrid+ygrid*ygrid+i/10.0))/2
        global dataX_0
        global dataY_0
        zgrid=np.sqrt(dataX_0**2+dataY_0**2)
        #print(zgrid)
        return xgrid, ygrid, zgrid

# вызов этой функции и дальше рисуем 3D график



for i in range (0, 100, 10):
    x, y, z = makeData(i)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_zlim([0,6])
    ax.plot_surface(x, y, z, rstride=4, cstride=4, cmap=cm.jet)
    
    filename = 'frames\step'+str(i)+'.png'
    plt.savefig(filename, dpi=96)
    plt.gca()
    #plt.show()

#Создание GIF из картинок
img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=200, loop=0)
