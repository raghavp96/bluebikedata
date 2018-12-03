import time
import threading
import json

import station_status
import station

api_svc_url = "http://api_svc:8080/"
test_api_svc_url = "http://localhost:8001/"

polling_md_functions = [
    {
        "Name": "Station Status Poller",
        "PollingFunction": station_status.poll,
        "Frequency": 10  # seconds
    },
    {
        "Name": "Station Information Poller",
        "PollingFunction": station.poll,
        "Frequency": 20  # seconds
    }
]


def scheduled_poll(name, poll_func, frequency):
    while(True):
        print(name, " - Starting")
        # response = poll_func(test_api_svc_url)
        response = poll_func(api_svc_url)
        print(name, " - ", response)
        time.sleep(frequency)
        print(threading.current_thread().getName(), " - Exiting")


def manage_threads():
    threads = []
    for polling_function in polling_md_functions:
        t = threading.Thread(
            name=polling_function["Name"], 
            target=scheduled_poll, 
            args=[
                polling_function["Name"], 
                polling_function["PollingFunction"], 
                polling_function["Frequency"], ])
        threads.append(t)
        t.start()


if __name__ == '__main__':
    manage_threads()