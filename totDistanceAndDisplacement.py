import pandas as pd
import csv
from csv import writer

def ngbrs(file):
    colnames = ['col', 'x', 'y']
    data = pd.read_csv(file, names = colnames)
    data = data.sort_values(by = ['x', 'y'])
    array2d = []
    for j in range(len(data.x.tolist())):
        array2d.append([j,data.x.tolist()[j], data.y.tolist()[j], 'no'])
    total = disp(array2d,0,0)
    array2d = []
    for j in range(len(data.x.tolist())):
        array2d.append([j,data.x.tolist()[j], data.y.tolist()[j], 'no'])
    total = distance_scalar(array2d, 0,0)
    return total

def ngbrs_array(file):
    colnames = ['col', 'x', 'y']
    data = pd.read_csv(file, names = colnames)
    data = data.sort_values(by = ['x', 'y'])
    array2d = []
    for j in range(len(data.x.tolist())):
        array2d.append([j,data.x.tolist()[j], data.y.tolist()[j], 'no'])
    outputarr = [0.00]
    ret = distance_scalar_array(array2d,0,outputarr)
    return ret

def ngbrs_displacement(file):
    colnames = ['col', 'x', 'y']
    data = pd.read_csv(file, names = colnames)
    data = data.sort_values(by = ['x', 'y'])
    array2d = []
    for j in range(len(data.x.tolist())):
        array2d.append([j,data.x.tolist()[j], data.y.tolist()[j], 'no'])
    arr = displacement_array(array2d,0,[float(0)])
    total = abs(arr[-1]-arr[0])
    return total

def ngbrs_displacement_array(file):
    colnames = ['col', 'x', 'y']
    data = pd.read_csv(file, names = colnames)
    data = data.sort_values(by = ['x', 'y'])
    array2d = []
    for j in range(len(data.x.tolist())):
        array2d.append([j,data.x.tolist()[j], data.y.tolist()[j], 'no'])
    outputarr = [0.00]
    ret = displacement_array(array2d,0,outputarr)
    return ret

def distance_scalar(data, idx, dis):
    filtered = []
    for d in data:
        if d[3] == 'no':
            filtered.append(1)
    if len(filtered) == 0:
        return 0
    if len(filtered) == 1:
        data[0][3] = 'yes'
        return dis
    else:
        data[idx][3] = 'yes'
        nearest = getNearest(data, idx)
        idxNearest = nearest[0]
        delta = nearest[1]
        return distance_scalar(data, idxNearest, dis + delta)

def distance_scalar_array(data, idx, dis):
    print(dis)
    filtered = []
    for d in data:
        if d[3] == 'no':
            filtered.append(1)
    if len(filtered) == 0:
        return dis
    if len(filtered) == 1:
        data[0][3] = 'yes'
        return dis
    else:
        data[idx][3] = 'yes'
        nearest = getNearest(data, idx)
        idxNearest = nearest[0]
        delta = nearest[1]
        newdis = float(dis[-1]) + float(delta)
        dis.append(newdis)
        return distance_scalar_array(data, idxNearest, dis)

def displacement_array(data, idx, dis):
    filtered = []
    for d in data:
        if d[3] == 'no':
            filtered.append(1)
    if len(filtered) == 0:
        return dis
    if len(filtered) == 1:
        data[0][3] = 'yes'
        return dis
    else:
        data[idx][3] = 'yes'
        nearest = getNearest(data, idx)
        idxNearest = nearest[0]
        delta = nearest[1]
        newdis = float(delta)
        dis.append(newdis)
        return displacement_array(data, idxNearest, dis)

def getNearest(data, idx):
    dislist = []
    indexlist = []
    for i in range(len(data)):
        if i == idx and data[i][3] == 'no':
            indexlist.append(i)
            dislist.append(999999999999999999999999)
        if i != idx and data[i][3] == 'no':
            indexlist.append(i)
            dis = (data[idx][1]-data[i][1])**2
            dis += (data[idx][2]-data[i][2])**2
            dislist.append(dis)
    return [indexlist[dislist.index(min(dislist))], min(dislist)]
