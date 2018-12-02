from flask import Flask, jsonify
import csv, json, requests
import trip_data

app = Flask(__name__)


@app.route('/')
def read_csv():
    result = {"trips":[]}
    with open('files/201810-bluebikes-tripdata.csv', newline='') as csv_file:
        fieldnames = ("tripduration","starttime","stoptime","start_station_id","start_station_name",
        "start_station_latitude","start_station_longitude","end_station_id","end_station_name",
        "end_station_latitude","end_station_longitude","bikeid","usertype","birthyear","gender")
        
        reader = csv.DictReader(csv_file, fieldnames)
        for row in reader:
            result.get("trips").append(row)
        # remove header row
        result.get("trips").pop(0)
        result2 = json.dumps(result)
        result2= json.loads(result2)
        trip_data.intoSQL(result2)
        return jsonify(result)



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)
    