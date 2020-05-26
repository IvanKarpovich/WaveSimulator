from matplotlib.colors import LinearSegmentedColormap
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import math

import glob
from PIL import Image

'''
Путь до картинок и до GIF
'''
fp_in = "frames\step*.png"
fp_out = "image.gif"

'''
Создание источника(координаты x и y, длина волны и период)
E(r, t)=E_0*cos(k*r + w*t + phi_0)
'''
def source(x, y, l, t, phi):
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
'''
Зеркальная поверхность с координатами
'''
'''
def mirrow(x_1, y_1, x_2, y_2):
    x_1 = xgrid-0.5
    global data
    data += np.cos(-np.sqrt(x_1*x_1+ygrid*ygrid)*2*math.pi/lam+2*math.pi/T*i+math.pi)
'''
'''
Неотражающая поверхность
'''
'''
def wall(x, y, x_1, y_1, x_2, y_2):
    if():
'''     
    
    
#fig = plt.figure()

'''
Параметры
'''
par_l = 1/5
par_t = 100

'''
Рисование N картинок
'''
for i in range (0, 100, 10):
    x_r = np.arange(-1, 1, 0.01)
    y_r = np.arange(-1, 1, 0.01)
    
    xgrid, ygrid = np.meshgrid(x_r, y_r)
    dataX_0 = xgrid-xgrid
    dataY_0 = xgrid-xgrid
    
    
    source(0.5, 0, par_l, par_t, 0)
    source(0.5, 0, par_l*2, par_t, 0)
    source(0.5, 0, par_l*4, par_t, 0)
    

    plt.imshow(np.sqrt(dataX_0**2+dataY_0**2),cmap=cm.seismic)

    filename = 'frames\step'+str(i)+'.png'
    plt.savefig(filename, dpi=96)
    plt.gca()
    
'''
Создание GIF из картинок
'''
img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=100, loop=0)
