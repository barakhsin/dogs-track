import pandas as pd
import subprocess
from time import sleep

def start_process(url):
    return subprocess.Popen(
        f"python worker.py {url}", shell=True, stdout=subprocess.PIPE)

def is_alive(process):
    return process.poll() is None

if __name__ == "__main__":
    n_urls = 10
    data = pd.read_csv("cameras_rtsp_urls1.csv")
    urls = data['rtsp'][:n_urls]

    print("WATCHDOG: Starting the processes...")
    processes = {
        url : start_process(url)
        for url in urls}
    print("WATCHDOG - Running...")

    while True:
        sleep(1)

        print("WATCHDOG - Number of alive processes:",
              sum([is_alive(process)
                   for process in processes.values()]))

        for url, process in processes.items():
            is_running = process.poll() is None
            if not is_running:
                print(f"WATCHDOG - Restarting the process for url {url}")
                processes[url] = start_process(url)
