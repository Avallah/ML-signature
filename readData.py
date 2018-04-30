import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Panda failed to load all the files (out of memory)
# We implemented our own data reader

def readData(pathToCsvFile, diff = False):
    # Read the data from the csv files
    # If diff = True, we preprocess the data by differentiating
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

# Read the info file with panda

def readInfoData(pathToCsvFile):
    out = pd.read_csv(pathToCsvFile)
    print("file " + pathToCsvFile + " read")
    return out