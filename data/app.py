from flask import Flask, jsonify
import time
import threading
import json

import station_status

app = Flask(__name__)

polling_md_functions = [
    {
        "Name" : station_status,
        "Frequency" : 20 #seconds
    }
]

# Figure out how to not hardcode this
api_svc_address = "http://api_svc"
api_svc_port = "8080"
# api_svc_url = api_svc_address + ":" + api_svc_port
api_svc_url = "http://localhost:8001"

@app.route('/csv')
def upload_csv():
    return jsonify("Not a feature yet...")

def poller(threads):    
    for func in polling_md_functions:
        process = threading.Thread(target=scheduled_poll, args=[func["Name"], "data-creator", func["Frequency"]])
        process.start()
        threads.append(process)

    for process in threads:
        process.join()

def scheduled_poll(poll_func, role, frequency):
    while(True):
        poll_func.poll(api_svc_url, role)
        time.sleep(frequency)

if __name__ == '__main__':
    threads = []
    #starts Flask app in separate thread on port 5000
    main_process = threading.Thread(target=app.run, args=[])
    main_process.start()
    threads.append(main_process)
    poller(threads)
    # app.run(debug=True,host='0.0.0.0', port=8080)
    