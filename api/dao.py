from db import queryDB
import datetime

class Station():

    def doGet(self, request_args, role="default"):
        result = {}
        select_statement = construct_select(request_args, "station", formatStationAttributeValue)
        result["stations"] = queryDB(select_statement, role)

        return result

class StationStatus():

    def doGet(self, request_args, role="default"):
        result = {}
        select_statement = construct_select(request_args, "station_status", formatStationStatusAttributeValue)
        result["station_statuses"] = queryDB(select_statement, role)

        return result

class Trip():

    def doGet(self, request_args, role="default"):
        result = {}
        select_statement = construct_select(request_args, "trip", formatTripAttributeValue)
        result["trips"] = queryDB(select_statement, role)

        return result

def construct_select(request_args, entity_name, whichFormatterFunc):
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

def formatStationAttributeValue(keyName, value):
    return str({
        "station_id" : value,
        "station_name" : "'" + value + "'",
        "latitude" : value,
        "longitude" : value,
        "short_name" : "'" + value + "'",
        "rental_methods" : "'" + value + "'",
        "capacity" : value,
        "rental_id" : value,
        "eightd_has_key_dispenser" : convertBool(value),
        "has_kiosk" : convertBool(value)
    }[keyName])


def formatStationStatusAttributeValue(keyName, value):
    return str({
        "station_status_id" : value,
        "station_id" : value,
        "num_bikes_available" : value,
        "num_ebikes_available" : value,
        "num_bikes_disabled" : value,
        "num_docks_available" : value,
        "num_dock_disabled" : value,
        "is_installed" : convertBool(value),
        "is_rented" : convertBool(value),
        "is_returning" : convertBool(value),
        "last_reported" : convertSecToTime(value),
        "eightd_has_available_keys" : convertBool(value)
    }[keyName])

def formatTripAttributeValue(keyName, value):
    return str({
        "trip_id" : value,
        "bike_id" : value,
        "start_time" : convertSecToTime(value),
        "end_time" : convertSecToTime(value),
        "usertype" : "'" + value + "'",
        "birthyear" : value,
        "gender" : convertGenderToId(value),
        "start_station" : value,
        "stop_station" : value        
    }[keyName])

def convertBool(val):
    if val == "true":
        return "TRUE"
    else:
        return "FALSE"


def convertGenderToId(val):
    if val == "F":
        return 1
    else:
        return 2

def convertSecToTime(val):
    return datetime.datetime.fromtimestamp(val)
