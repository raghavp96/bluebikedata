from flask import Flask, jsonify
import simplejson
import json
from db import connect


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
def query(querySQL):
    resultsArray = []
    querySQL = querySQL.replace("%20", " ")

    if (querySQL.startswith("select")):
        db = connect()

        try: 
            cursor = db.cursor()
            cursor.execute(querySQL)

            row_headers = [x[0] for x in cursor.description]
            resultset = cursor.fetchall()

            for result_item in resultset:
                resultsArray.append(dict(zip(row_headers, result_item)))

            db.close()
        except Error as err:
            resultsArray.append("Something went wrong: {}".format(err))
    
    else:
        resultsArray.append("Only SELECT queries are allowed") 

     
    result = {
        "result" : resultsArray
    }

    return jsonify(json.loads(simplejson.dumps(result, use_decimal=True)))

@app.route('/mutate/<querySQL>')
def mutate(querySQL):
    resultsArray = []
    querySQL = querySQL.replace("%20", " ")

    if (querySQL.startswith("select")):
        db = connect()

        cursor = db.cursor()
        cursor.execute(querySQL)
        db.commit()

        db.close()
    
    else:
        resultsArray.append("Only SELECT queries are allowed") 

     
    result = {
        "result" : resultsArray
    }

    return jsonify(json.loads(simplejson.dumps(result, use_decimal=True)))


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)
