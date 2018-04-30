import signature as sn
import numpy as np
import esig.tosig as ts

from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn import linear_model

# We split the data set according to the test size
def splitDataSet(listpath, testsize,order):
    signatures = sn.calculateMultipleSignatures(listpath, order)
    Y = [listpath[i][2] for i in range(len(listpath))]
    X_train, X_test, Y_train, Y_test = train_test_split(signatures, Y,test_size=testsize, random_state=0)
    return [X_train, X_test, Y_train, Y_test]

# Function giving the prediction error
def predictionError(X,Y,lm):
    tmp = lm.predict(X)
    pred = [1 if tmp[i] >= 0.5 else 0 for i in range(len(tmp))] 
    return sum([abs(Y[i]-pred[i]) for i in range(len(Y))])/len(Y)
    
# Fit a linear model
def linearRegression(listpath,testsize,order):
    [X_train, X_test, Y_train, Y_test]= splitDataSet(listpath, testsize,order)
    lm = linear_model.LinearRegression()
    lm.fit(X_train,Y_train)
    
    out_train = predictionError(X_train,Y_train,lm)
    out_test = predictionError(X_test,Y_test,lm)

    return [out_train,out_test]