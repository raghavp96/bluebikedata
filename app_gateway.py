from flask import Flask, jsonify, request, redirect, url_for
import requests
import os
import json


app = Flask(__name__)

api_svc_url = os.getenv("API_SVC_URL", "http://localhost:8001/")
trip_data_svc_url = os.getenv("TRIP_DATA_SVC_URL", "http://localhost:8003/")

@app.route('/api')
def hello_world():
    return jsonify(requests.get(api_svc_url).json())

@app.route('/api/station_status_latest_id', methods=['GET'])
def query_latest_station_status_id(role="default"):
    return jsonify(requests.get(api_svc_url + "station_status_latest_id").json())

@app.route('/api/trip_latest_id', methods=['GET'])
def query_latest_trip_status_id(role="default"):
    return jsonify(requests.get(api_svc_url + "trip_latest_id").json())


@app.route('/api/station_status/latest', methods=['GET'])
def query_latest_station_status(role="default"):
    return jsonify(requests.get(api_svc_url + "station_status/latest").json())


@app.route('/api/<entity>', methods=['GET'])
@app.route('/api/<entity>/<role>/', methods=['GET', 'POST'])
def query_entity(entity, role="default"):
    if request.method == 'GET':
        return jsonify(requests.get(api_svc_url + entity).json())
    elif request.method == 'POST':
        headers = {'Content-type': 'application/json; charset=UTF-8'}
        jsons = json.load(request.get_json())
        resp = requests.post(api_svc_url + entity + "/" + role, headers=headers, json=jsons).json()
        return jsonify(resp)
    return redirect(api_svc_url)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
