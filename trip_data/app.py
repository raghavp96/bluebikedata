from flask import Flask, jsonify
import csv, json, requests
import trip_data

app = Flask(__name__)

api_svc_address = "http://localhost"
api_svc_port = "8001"
api_svc_endpoint = "/"

api_svc_url= api_svc_address + ":" + api_svc_port + api_svc_endpoint


def post_trips():
    post_data = {"trips":[]}
    current_trip_ids = get_trip_ids()

    with open('files/201810-bluebikes-tripdata.csv', newline='') as csv_file:
        fieldnames = ("tripduration","starttime","stoptime","start_station_id","start_station_name",
        "start_station_latitude","start_station_longitude","end_station_id","end_station_name",
        "end_station_latitude","end_station_longitude","bikeid","usertype","birthyear","gender")
        
        reader = csv.DictReader(csv_file, fieldnames)
        for row in reader:
            post_data.get("trips").append(row)


        # remove header row
        post_data.get("trips").pop(0)
        post_data = json.dumps(post_data)
        post_data= json.loads(post_data)
        r=requests.post(api_svc_url + "trip/data-creator/", json=post_data)
        print(r.content)


def get_trips():
    url = api_svc_url + "trip"
    trips = requests.get(url).json()["trips"]
    return trips

def get_trip_ids():
    trips= get_trips()
    if len(trips)==0:
        return []
    else:
        trip_ids=trips["trip_id"]
        return trip_ids
        
post_trips()

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)
    