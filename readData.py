import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#We implement our own reader instead of using panda, because panda failed for files that are too big 
def readData(pathToCsvFile, diff = True): #diff: preprocessing of the data by differenciation
    out = []
    with open(pathToCsvFile) as f:
        f.readline()
        for line in f:
            line = line.replace('"', '').strip().split(',')
            if diff != True:
                out.append([line[0],np.array([float(x) for x in line[1:] if x != '']).reshape((-1,1))]) #need to reshape for the signature
            else: 
                tmp = np.diff([float(x) for x in line[1:] if x != ''])
                out.append([line[0],np.array(tmp[1:-1]).reshape((-1,1)), 1 if tmp[-1] >= 0 else 0])
        print("file " + pathToCsvFile + " read")
    return out

#Read the info file with panda
def readInfoData(pathToCsvFile):
    out = pd.read_csv(pathToCsvFile)
    print("file " + pathToCsvFile + " read")
    return out