from flask import Flask, jsonify
import csv, json

app = Flask(__name__)

@app.route('/')
def read_csv():
    result = []
    with open('files/201810-bluebikes-tripdata.csv', newline='') as csv_file:
        fieldnames = ("tripduration","starttime","stoptime","start_station_id","start_station_name",
        "start_station_latitude","start_station_longitude","end_station_id","end_station_name",
        "end_station_latitude","end_station_longitude","bikeid","usertype","birth year","gender")
        
        reader = csv.DictReader(csv_file, fieldnames)
        for row in reader:
            result.append(row)
        # remove header row
        result.pop(0)
        return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)
    