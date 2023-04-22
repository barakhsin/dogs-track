import numpy as np
from pathlib import Path
def numbers(a):
    empty_array = np.empty((0)) # create empty array
    for path in Path('/home/sparklab/yolov8_tracking/runs/track/').glob(a+'*/*_maxID.txt'): # search through maxID files in folder
        file1 = open(path.resolve()) # open file
        while True: 
            # считываем строку
            line = file1.readline() # read line with maxID
            if line != '':
                empty_array = np.append(empty_array, [int(line)])   # append maxID to array
            if not line:
                break
    return(empty_array)