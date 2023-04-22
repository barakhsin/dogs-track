# Python Estimator module for dog tracker
import json
import numpy as np
import datetime as dt
import requests

step = 1.0/30.0
N = 10 # ten region of Yakutsk
sqr = np.array([6.006, 11.851, 7.206, 1.748, 17.642, 16.248, 23.919, 13.604, 3.437, 19.96]) # square of regions of Yakutsk
spq = np.array([1.1, 1.02, 1.0, 1.04, 1.11, 1.08, 1.15, 1.07, 0.97, 1.07]) # power of region

from max_id import numbers
# testcamNumb=([5.0, 2.0, 4.0])
testcamNumb = np.load('numbers.npy')
print(testcamNumb)
# For example we have vector - number of dogs fixed by camera inside week, cameras a fixed
# camNumb[0] -- first camera, ..., camNumb[N-1] -- camera number N
def estDogs(camNumb):
    oldnr = np.load('temp.npy')
    dailycoef = (dt.datetime.today().weekday()+1.0) / 7.0
    w = np.ones(len(camNumb))
    tarr = np.zeros((N, len(camNumb)))
    sqc = np.ones(len(camNumb))
    for j in range(len(camNumb)):
        for i in range(N):
            tarr[i, j] = camNumb[j]*sqr[i]*spq[i]/(dailycoef*sqc[j])
    nr = np.dot(tarr, w) / len(camNumb)
    nr = oldnr + step*(nr - oldnr)
    nr = (np.rint(nr)).astype(int)
    np.save('temp.npy', nr)
    sumnr = np.sum(nr)
    nr = np.append(nr, sumnr)
    return nr

def prepData(sendnr):
    nr = sendnr
    nr_list = nr.tolist()
    data = [{"quantity": x} for x in nr_list]
    with open("QTY.json", "w") as outfile:
        json.dump(data, outfile)
    with open('./CONST.json', 'r') as f:
        constdata = json.load(f)
    merged_array = []
    for i in range(len(constdata)):
        merged_array.append({**constdata[i], **data[i]})
    with open("MOCK_DATA.json", "w") as mockfile:
        json.dump(merged_array, mockfile)

def sendData():
    # Set the URL 
    url = "http://5.159.101.236:3001"

    # Create the data to send as a dictionary 
    with open('./MOCK_DATA.json', 'r') as f:
        data = json.load(f)

    # Convert the data to JSON format 
    json_data = json.dumps(data) 

    # Set the content type to JSON 
    headers = {'Content-Type': 'application/json'} 

    # Make the POST request to the API endpoint with the JSON data 
    response = requests.post(url, data=json_data, headers=headers) 

    # Print the response status code 
    if response.status_code == 200:
        print('Data transfered successfully')

def estSend(camNumb):
    nr = estDogs(camNumb)
    prepData(nr)
    sendData()
    return 2507.0
        
print(estSend(testcamNumb))
