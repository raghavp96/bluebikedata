from flask import Flask, jsonify, request
from db import queryDB, mutateDB

import simplejson
import json

from dao import doGet, doPost

app = Flask(__name__)


@app.route('/')
def hello_world():
    info = {
        "UserType": ["Unauthenticated", "Authenticated"],
        "Requests": [
            {
                "Type": "GET",
                "Path": "/<entity>",
                "PathDetails": [
                    "See the docs for how to properly query"
                ]
            },
            {
                "Type": "POST",
                "Path": "/<entity>",
                "PathDetails": [
                    "See the docs for how to properly query",
                    "Only authenticated users can make POST requests"
                ]
            }
        ]
    }
    return jsonify(info)


@app.route('/station_status/latest_id', methods=['GET'])
def query_latest_station_status_id(role="default"):
    # ignores request.args
    station_statuses = doGet("station_status", {}, role)[
        "station_statuses"]

    latest_station_status_id = 0 if len(
        station_statuses) == 0 else station_statuses[-1]["station_status_id"]

    return jsonify({ "latest_station_status_id" : latest_station_status_id })


@app.route('/station_status/latest', methods=['GET'])
def query_latest_station_status(role="default"):
    station_statuses = doGet("station_status", request.args, role)[
        "station_statuses"]

    last_station_status_id = 0 if len(
        station_statuses) == 0 else station_statuses[-1]["station_status_id"]

    args = dict(request.args)
    args["station_status_id"] = last_station_status_id

    return jsonify(doGet("station_status", args, role)["station_statuses"])


@app.route('/<entity>', methods=['GET'])
@app.route('/<entity>/<role>/', methods=['GET', 'POST'])
def query_entity(entity, role="default"):
    if request.method == 'GET':
        return jsonify(doGet(entity, request.args, role))
    elif request.method == 'POST':
        return jsonify(doPost(entity, request.get_json(), role))
    else:
        return "NOT SUPPORTED"


# Removing the ability for users to inject SQL into browser
# Unsafe operation - not RESTful
# @app.route('/query/<querySQL>')
# @app.route('/query/<querySQL>/<role>')
# def query(querySQL, role="default"):
#     result = {}
#     resultsArray = []
#     querySQL = querySQL.replace("%20", " ")
#     if (querySQL.startswith("select")):
#         result["result"] = queryDB(querySQL, role)
#     else:
#         resultsArray.append("Only SELECT queries are allowed")
#         result["result"] = resultsArray
#     return jsonify(json.loads(simplejson.dumps(result, use_decimal=True)))
# @app.route('/mutate/<querySQL>')
# @app.route('/mutate/<querySQL>/<role>')
# def mutate(querySQL, role="default"):
#     result = {}
#     querySQL = querySQL.replace("%20", " ")
#     if (querySQL.startswith("insert")):
#         result["result"] = mutateDB(querySQL, role)
#     else:
#         result["result"] = "Only INSERT queries are allowed"
#     return jsonify(json.loads(simplejson.dumps(result)))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
