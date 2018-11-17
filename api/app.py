from flask import Flask, jsonify
from db import queryDB, mutateDB

import simplejson
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    info = {
        "UserType" : [ "Unauthenticated", "Authenticated"],
        "Requests" : [
            {
                "Type" : "GET",
                "Path" : "/query/<querySQL>",
                "PathDetails" : [
                    "Query SQL must be separated by '%20' in place of spaces",
                    "Only SELECT Statements allowed",
                    "Unauthenticated users and authenticated users can access"
                ]
            },
            {
                "Type" : "GET",
                "Path" : "/mutate/<querySQL>",
                "PathDetails" : [
                    "Query SQL must be separated by '%20' in place of spaces",
                    "Only INSERT or UPDATE Statements allowed",
                    "Only authenticated users can access"
                ]
            }
        ]
    }
    return jsonify(info)

@app.route('/query/<querySQL>')
@app.route('/query/<querySQL>/<role>')
def query(querySQL, role="default"):
    result = {}
    resultsArray = []
    querySQL = querySQL.replace("%20", " ")

    if (querySQL.startswith("select")):
        result["result"] = queryDB(querySQL, role)
    else:
        resultsArray.append("Only SELECT queries are allowed") 
        result["result"] = resultsArray

    return jsonify(json.loads(simplejson.dumps(result, use_decimal=True)))

@app.route('/mutate/<querySQL>')
@app.route('/mutate/<querySQL>/<role>')
def mutate(querySQL, role="default"):
    result = {}
    querySQL = querySQL.replace("%20", " ")

    if (querySQL.startswith("insert")):
        result["result"] = mutateDB(querySQL, role)
    else:
        result["result"] = "Only INSERT queries are allowed"

    return jsonify(json.loads(simplejson.dumps(result)))


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)