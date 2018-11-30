from db import queryDB
import datetime

## dao.py: Transforms GET/POST requests into appropriate SQL queries and sends to db.py
#  - Public Methods: doGet and doPost

def doGet(entity, request_args, role="default"):
    result = {}
    if entity == "station":
        select_statement = __construct_select(request_args, "station", __formatStationAttributeValue)
        result["stations"] = queryDB(select_statement, role)
    elif entity == "station_status":
        select_statement = __construct_select(request_args, "station_status", __formatStationStatusAttributeValue)
        result["station_statuses"] = queryDB(select_statement, role)
    elif entity == "trip":
        select_statement = __construct_select(request_args, "trip", __formatTripAttributeValue)
        result["trips"] = queryDB(select_statement, role)
    else:
        result["error"] = "Unknown entity"
    
    return result

def __construct_select(request_args, entity_name, whichFormatterFunc):
    query = "select * from " + entity_name

    if request_args == {}:
        query += ";"
    else:
        query += " where "

    for key, value in request_args.items():
        query += key + " = " + whichFormatterFunc(key, value)
        if key == sorted(request_args.keys())[-1]:
            query += ";"
        else:
            query += " and "

    print("Query: " + query)
    
    return query

def __formatStationAttributeValue(keyName, value):
    return str({
        "station_id" : value,
        "station_name" : "'" + value + "'",
        "latitude" : value,
        "longitude" : value,
        "short_name" : "'" + value + "'",
        "rental_methods" : "'" + value + "'",
        "capacity" : value,
        "rental_id" : value,
        "eightd_has_key_dispenser" : __convertBool(value),
        "has_kiosk" : __convertBool(value)
    }[keyName])


def __formatStationStatusAttributeValue(keyName, value):
    return str({
        "station_status_id" : value,
        "station_id" : value,
        "num_bikes_available" : value,
        "num_ebikes_available" : value,
        "num_bikes_disabled" : value,
        "num_docks_available" : value,
        "num_dock_disabled" : value,
        "is_installed" : __convertBool(value),
        "is_rented" : __convertBool(value),
        "is_returning" : __convertBool(value),
        "last_reported" : __convertSecToTime(value),
        "eightd_has_available_keys" : __convertBool(value)
    }[keyName])

def __formatTripAttributeValue(keyName, value):
    return str({
        "trip_id" : value,
        "bike_id" : value,
        "start_time" : __convertSecToTime(value),
        "end_time" : __convertSecToTime(value),
        "usertype" : "'" + value + "'",
        "birthyear" : value,
        "gender" : __convertGenderToId(value),
        "start_station" : value,
        "stop_station" : value        
    }[keyName])

def __convertBool(val):
    if val == "true":
        return "TRUE"
    else:
        return "FALSE"


def __convertGenderToId(val):
    if val == "F":
        return 1
    else:
        return 2

def __convertSecToTime(val):
    return datetime.datetime.fromtimestamp(val)
