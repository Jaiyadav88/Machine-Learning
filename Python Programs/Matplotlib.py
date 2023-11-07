import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
from itertools import count
import pandas as pd

plt.style.use('fivethirtyeight')
x_vals=[0,1,2,5,8,9]
y_vals=[2,1,6,3,9,7]
#static graph
# plt.plot(x_vals,y_vals)
# plt.tight_layout()
# plt.show()

x_vals=[]
y_vals=[]
#creating dynamic graph
index=count()#counts numbers one after another(eg:1,2,3,4)


# def animate(i):
#     x_vals.append(next(index))#counts numbers regularly
#     y_vals.append(random.randint(0,5))
#     plt.cla() #clear axis previous graph
#     plt.plot(x_vals,y_vals)



def animate(i):
    df=pd.read_csv('data.csv')
    x=df['x_value']
    y1=df['total_1']
    y2=df['total_2']
    plt.cla() #clear axis previous graph
    plt.plot(x,y1,label='channel 1')
    plt.plot(x,y2,label='channel 2')
    plt.legend(loc='upper left')
    plt.tight_layout()

ani=FuncAnimation(plt.gcf(),animate,interval=1000)
plt.tight_layout()
plt.show()
    

