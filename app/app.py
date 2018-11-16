from flask import Flask, jsonify
import simplejson
import json
from db import connect


app = Flask(__name__)

@app.route('/')
def hello_world():
    db = connect('creator')

    cursor = db.cursor()

    # Execute SQL select statement
    cursor.execute("SELECT * FROM station")
    # Get the number of rows in the resultset
    numrows = cursor.rowcount
    print(numrows)

    cursor.execute("delete from station where station_id=5")
    db.commit()

    cursor.execute(
        "insert into station(station_id, station_name, latitude, longitude, short_name, rental_methods, capacity, rental_id, eightd_has_key_dispenser, has_kiosk) values" +
        "(5, 'Northeastern University - North Parking Lot', 42.341814, -71.090179, 'B32012', 'CREDITCARD', 15, 'https://www.bluebikes.com/app?station_id=5',false, true)")
    db.commit()

    # Execute SQL select statement
    cursor.execute("SELECT * FROM station")
    # Get the number of rows in the resultset
    numrows = cursor.rowcount
    print(numrows)

    # Get and display one row at a time
    for x in range(0, numrows):
        row = cursor.fetchone()
        print(row)

    # Close the connection
    db.close()
    return 'Flask Dockerized'


@app.route('/<role>/query/<querySQL>')
def query(role, querySQL):
    resultsArray = []
    querySQL = querySQL.replace("%20", " ")

    if (role == 'app' and querySQL.startswith("select")):
        db = connect(role)

        cursor = db.cursor()
        cursor.execute(querySQL)

        row_headers = [x[0] for x in cursor.description]
        resultset = cursor.fetchall()

        for result_item in resultset:
            resultsArray.append(dict(zip(row_headers, result_item)))

        db.close()
    elif (role == 'creator' and querySQL.startswith("select")):
        db = connect(role)

        cursor = db.cursor()
        cursor.execute(querySQL)
        numrows = cursor.rowcount

        for x in range(0, numrows):
            resultsArray.append(cursor.fetchone())
        
        db.close()
    elif (role == 'creator' and querySQL.startswith("insert")):
        db = connect(role)

        cursor = db.cursor()
        cursor.execute(querySQL)
        db.commit()
        numrows = cursor.rowcount

        for x in range(0, numrows):
            resultsArray.append(cursor.fetchone())
        
        db.close()
    else:
        resultsArray.append("Either role (", role ,") or SQL query (", querySQL, ") not allowed") 

     
    result = {
        "result" : resultsArray
    }

    return jsonify(json.loads(simplejson.dumps(result, use_decimal=True)))


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)
