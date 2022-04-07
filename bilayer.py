import numpy as np
import random

def getxy(box_x,box_y):
    x = random.uniform(0,(box_x))
    y = random.uniform(0,(box_y))
    return(x,y)

def unique_rows(a):
    a = np.ascontiguousarray(a)
    unique_a = np.unique(a.view([('', a.dtype)]*a.shape[1]))
    return list(unique_a.view(a.dtype).reshape((unique_a.shape[0], a.shape[1])))

def setLipids(box_x,box_y,box_z,N):
    pos = []
    high = int(box_z/2)+3
    low = int(box_z/2)-3
    poss = np.zeros((box_x,box_y))
    while len(pos) < N*3:
        n = len(pos)/3
        x,y = getxy(box_x-1,box_y-1)
        if n <= int(N/2):
            z = high
            pos.append([x,y,z])
            pos.append([x,y,z -1])
            pos.append([x,y,z -2])
        else:
            z = low
            pos.append([x,y,z])
            pos.append([x,y,z +1])
            pos.append([x,y,z +2])
        #pos = unique_rows(pos)
    pos = np.array(pos)
    return(pos)

def perfLipids(box):
    pos = []
    lat = np.arange(-box/2,(box/2)-1,1)
    high = 3
    low = -3
    for i in lat:
        for j in lat:
            pos.append([i,j,high])
            pos.append([i,j,high-1])
            pos.append([i,j,high-2])
            pos.append([i,j,low])
            pos.append([i,j,low+1])
            pos.append([i,j,low+2])
    pos = np.array(pos)
    return(pos)

def hexLipids(box):
    xstep = 2**(1/6)*1.05
    ystep = 2**(1/6)*1.05*(3**(1/2)/2)
    high = 3
    low = -3
    y = 0
    pos = []
    boxy = int(box/(ystep))
    boxx = int(box/(xstep))
    for j in range(boxy):
        x = j*(xstep/2)
        for i in range(boxx):
            pos.append([x,y,high])
            pos.append([x,y,high-1])
            pos.append([x,y,high-2])
            pos.append([x,y,low])
            pos.append([x,y,low+1])
            pos.append([x,y,low+2])
            x+=xstep
        y += ystep
    return np.array(pos), boxx*xstep, boxy*ystep
        
