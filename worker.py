import sys
from time import sleep
import numpy as np

def is_crashed(probability_to_crash = 0.03):
    # generating a random number and if small enough - simulating a crash
    return np.random.uniform(0, 1) < probability_to_crash

if __name__ == "__main__":
    url = sys.argv[1]
    print("TRAKER - started for url:", url)

    while not is_crashed():
        #print("Alive for url:", url)
        sleep(1)

    print("TRACKER - crashed:", url)
