import numpy as np
import esig.tosig as ts
import sklearn

# Calculate the signature for one path
def calculateSignature(path,order):
    time = np.array(range(len(path[1]))).reshape((-1,1))
    two_dim_stream = np.append(path[1],time, axis=1)
    out = ts.stream2sig(two_dim_stream, 2)[1:]
    return out

# Calculate the signature for a list of paths
def calculateMultipleSignatures(listpath,order):
    signatures = [calculateSignature(listpath[i],2) for i in range(len(listpath))]
    print("Signature calculated at order " + str(order) +" for all paths")
    return signatures