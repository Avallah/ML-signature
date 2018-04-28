import matplotlib.pyplot as plt
import numpy as np

def readData(pathToCsvFile):
    out = []
    i = 0
    with open(pathToCsvFile) as f:
        f.readline()
        for line in f:
            line = line.replace('"', '').strip().split(',')
            out.append([line[0],[float(x) for x in line[1:] if x != '']])
    return out

