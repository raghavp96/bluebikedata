from flask import Flask, jsonify
import csv, json, requests


app = Flask(__name__)

api_svc_address = "http://localhost"
api_svc_port = "8001"
api_svc_endpoint = "/"

api_svc_url= api_svc_address + ":" + api_svc_port + api_svc_endpoint

def default_convert_csv_to_json():
    post_data = {"trips":[]}
    with open('files/201810-bluebikes-tripdata.csv', newline='') as csv_file:
        fieldnames = ("tripduration","start_time","end_time","start_station","start_station_name",
        "start_station_latitude","start_station_longitude","stop_station","end_station_name",
        "end_station_latitude","end_station_longitude","bike_id","usertype","birthyear","gender")
        
        reader = csv.DictReader(csv_file, fieldnames)
        latest_trip_id=requests.get(api_svc_url+"trip_latest_id").json()["latest_trip_id"]
        for row in reader:
            # Add the trip id to the JSON
            latest_trip_id=latest_trip_id+1
            row.update({'trip_id':latest_trip_id})
            row.move_to_end('trip_id', last=False)
            post_data.get("trips").append(row)
        
        
    # remove header row
    print('do')
    r=requests.post(api_svc_url + "trip/data-creator/", json=json.dumps(post_data["trips"]))
    print(r.content)

    return r
default_convert_csv_to_json()


@app.route('/csv', methods=['POST'])
def upload_csv():
    return jsonify("To Do")

    
