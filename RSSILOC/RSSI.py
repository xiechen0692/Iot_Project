import csv
import os
import numpy as np
from sklearn.metrics import mean_squared_error
#L=np.array(np.zeros((3*94))).reshape(94,3)
column=[]
input=[-54,-52,-52,-42]
input_w=[]
RSSI=[]
for i in range(4):
    if input[i]>-30:
        w=0.5
    elif -30>input[i] >= -40:
        w = 0.25
    elif -40 > input[i] >= -50:
        w = 0.15
    elif -50>input[i] >= -60:
        w = 0.05
    elif -60>input[i] >= -70:
        w = 0.03
    elif -70>input[i] >= -80:
        w = 0.02
    input_w.append(input[i]*w)
input_w_arr=np.array(input_w)

# w=
# a = numpy.array((xa ,ya, za))
# b = numpy.array((xb, yb, zb))
# dist = numpy.linalg.norm(a-b)
with open('RSSI.csv','r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for i, j in enumerate(reader):
        for k in range(1,95):
            if i == k:
                column.append(j)    #0~93

for i in range(93):
    RSSI.append(column[i][0].split()[3:7])
RSSI_w=np.zeros(93*4).reshape(93,4)
RSSI_single=np.zeros(1*4).reshape(1,4)
for j in range(93):
    for i in range(4):
        if int(RSSI[j][i])>-30:
            w=0.5
        elif -30>int(RSSI[j][i]) >= -40:
            w = 0.25
        elif -40 > int(RSSI[j][i]) >= -50:
            w = 0.15
        elif -50>int(RSSI[j][i]) >= -60:
            w = 0.05
        elif -60>int(RSSI[j][i]) >= -70:
            w = 0.03
        elif -70>int(RSSI[j][i]) >= -80:
            w = 0.02
        RSSI_single[0,i]=(int(RSSI[j][i])*w)
        RSSI_w[j,:]= RSSI_single[0,:]
mse_arr=np.array(np.zeros((1*93))).reshape(93,1)
for i in range(93):
    mse_arr[i] = mean_squared_error(input_w_arr, RSSI_w[i,:])
mse_arr=mse_arr.reshape(93,)
loc_min=np.where(mse_arr == mse_arr.min())
column[loc_min[0][0]][0].split()
x=int(column[loc_min[0][0]][0].split()[0])
y=int(column[loc_min[0][0]][0].split()[1])
z=int(column[loc_min[0][0]][0].split()[2])
x1=87
y1=85
z1=6
stringx="curl -i -XPOST 'http://140.112.18.229:32071/write?db=ntu_iot' --data-binary 'team11,axis=x value='"+str(x1)
stringy="curl -i -XPOST 'http://140.112.18.229:32071/write?db=ntu_iot' --data-binary 'team11,axis=y value='"+str(y1)
stringz="curl -i -XPOST 'http://140.112.18.229:32071/write?db=ntu_iot' --data-binary 'team11,axis=z value='"+str(z1)

os.popen(stringx).read()
os.popen(stringy).read()
os.popen(stringz).read()