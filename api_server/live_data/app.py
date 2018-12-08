import time
import threading
import json
import os

import station_status
import station

api_svc_url = os.getenv("API_SVC_URL", "http://localhost:8001/")

polling_md_functions = [
    {
        "Name": "Station Status Poller",
        "PollingFunction": station_status.poll,
        "Frequency": 600  # seconds, 10 minutes
    },
    {
        "Name": "Station Information Poller",
        "PollingFunction": station.poll,
        "Frequency": 86400  # seconds, 24 hrs
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