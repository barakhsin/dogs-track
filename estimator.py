# Python Estimator module for dog tracker
import numpy as np
import datetime as dt
step = 1.0/30.0
N = 10 # ten region of Yakutsk
sqr = np.array([6.006, 11.851, 7.206, 1.748, 17.642, 16.248, 23.919, 13.604, 3.437, 19.96]) # square of regions of Yakutsk
spq = np.array([1.1, 1.02, 1.0, 1.04, 1.11, 1.08, 1.15, 1.07, 0.97, 1.07]) # power of region
testoldnr = np.array([193.0,444.0, 256.0, 68.0, 666.0, 521.0, 1161.0, 643.0, 92.0, 779.0])
testcamNumb=([5.0, 2.0, 4.0])
# For example we have vector - number of dogs fixed by camera inside week, cameras a fixed
# camNumb[0] -- first camera, ..., camNumb[N-1] -- camera number N
def estDogs(oldnr, camNumb):
    dailycoef = (dt.datetime.today().weekday()+1.0) / 7.0
    w = np.ones(len(camNumb))
    tarr = np.zeros((N, len(camNumb)))
    sqc = np.ones(len(camNumb))
    for j in range(len(camNumb)):
        for i in range(N):
            tarr[i, j] = camNumb[j]*sqr[i]*spq[i]/(dailycoef*sqc[j])
    nr = np.dot(tarr, w) / len(camNumb)
    nr = oldnr + step*(nr - oldnr)
    return nr
print(estDogs(testoldnr, testcamNumb))