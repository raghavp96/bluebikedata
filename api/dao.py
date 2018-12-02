from db import queryDB, mutateDB
from formatter import formatStationAttributeValue, formatStationStatusAttributeValue, formatTripAttributeValue
from formatter import reverseformatStationAttributeValue, reverseFormatStationStatusAttributeValue, reverseFormatTripAttributeValue

# dao.py: Transforms GET/POST requests into appropriate SQL queries and 
# sends to db.py
#  - Public Methods: doGet and doPost

# The entity map allows us to write more generic code, agnostic of what 
# entity we're actually dealing with

entityMap = {
    "station": {
        "tableName": "station",
        "entityPlural": "stations",
        "formatter": formatStationAttributeValue,
        "reverser": reverseformatStationAttributeValue,
        "columnOrderings": [
            "station_id",
            "station_name",
            "latitude",
            "longitude",
            "short_name",
            "rental_methods",
            "capacity",
            "rental_id",
            "eightd_has_key_dispenser",
            "has_kiosk"
        ]
    },
    "station_status": {
        "tableName": "station_status",
        "entityPlural": "station_statuses",
        "formatter": formatStationStatusAttributeValue,
        "reverser": reverseFormatStationStatusAttributeValue,
        "columnOrderings": [
            "station_status_id",
            "station_id",
            "num_bikes_available",
            "num_ebikes_available",
            "num_bikes_disabled",
            "num_docks_available",
            "num_dock_disabled",
            "is_installed",
            "is_rented",
            "is_returning",
            "last_reported",
            "eightd_has_available_keys"
        ]
    },
    "trip": {
        "tableName": "trip",
        "entityPlural": "trips",
        "formatter": formatTripAttributeValue,
        "reverser": reverseFormatTripAttributeValue,
        "columnOrderings": [
            "trip_id",
            "bike_id",
            "start_time",
            "end_time",
            "usertype",
            "birthyear",
            "gender",
            "start_station",
            "stop_station"
        ]
    }
}

# Converts GET request into appropriate SELECT and queries DB, returning a 
# dict with results array


def doGet(entity, request_args, role="default"):
    result = {}

    entityDict = entityMap.get(entity)

    if entityDict is not None:
        select_statement = __construct_select(
            request_args, entityDict["tableName"], entityDict["formatter"])
        result[entityDict["entityPlural"]] = queryDB(select_statement, role)
        # result[entityDict["entityPlural"]] = reverseFormatJSON(
        #     queryDB(select_statement, role))
    else:
        result["error"] = "Unknown entity"

    return result

# Converts POST request into appropriate INSERT and queries DB, returning a 
# dict with a success message


def doPost(entity, request_json_data, role="default"):
    result = {}
    if role == "default":
        result["error"] = "Access Denied"
    elif (request_json_data == None) or (request_json_data == {}):
        result["error"] = "No values to insert"
    else:
        entityDict = entityMap.get(entity)
        if entityDict is not None:
            insert_statement = ""
            try:
                if isSingleInsert(request_json_data, entity):
                    insert_statement += __construct_insert(
                        request_json_data, 
                        entityDict["tableName"], 
                        entityDict["formatter"], 
                        entityDict["columnOrderings"], 
                        False, entity)
                else:
                    insert_statement += __construct_insert(
                        request_json_data, 
                        entityDict["tableName"], 
                        entityDict["formatter"], 
                        entityDict["columnOrderings"], 
                        True, entityDict["entityPlural"])

                result[entityDict["entityPlural"]] = mutateDB(
                    insert_statement, role)
            except KeyError as err:
                result["error"] = "Bad request JSON data key: " + str(err)
        else:
            result["error"] = "Unknown entity"

    return result


# Constructs a valid SELECT statment for an entity, with the given arguments 
# in `request_args`
def __construct_select(request_args, entity_table_name, formatterFunc):
    query = "select * from " + entity_table_name

    if request_args == {}:
        query += ";"
    else:
        query += " where "

    for key, value in request_args.items():
        query += key + " = " + formatterFunc(key, value)
        if key == sorted(request_args.keys())[-1]:
            query += ";"
        else:
            query += " and "

    print("Query: " + query)

    return query


# Given an entity name looks at the JSON data if either the entityName or its 
# plural form are there.
def isSingleInsert(request_json_data, entity_name):
    try:
        request_json_data[entity_name]
        return True
    except KeyError:
        try:
            request_json_data[entityMap[entity_name]["entityPlural"]]
            return False
        except KeyError as err:
            raise err


# Constructs a valid INSERT statment for an entity, with the given arguments in 
# `request_args`
def __construct_insert(
    request_json_data, entity_table_name, formatterFunc, columnOrderings, 
    isMultiple, entry_data_key):
    query = "insert into " + entity_table_name + " values "

    if not isMultiple:
        new_entity = request_json_data[entry_data_key]
        if new_entity is not None:  # only inserting one entity
            query += __insertOneRow(new_entity,
                                    formatterFunc, columnOrderings) + ";"
        return query

    else:
        new_entities = request_json_data[entry_data_key]
        if new_entities is not None:
            for index, entity in enumerate(new_entities):
                if index == len(new_entities) - 1:
                    query += __insertOneRow(entity,
                                            formatterFunc, columnOrderings)
                    query += ";"
                else:
                    query += __insertOneRow(entity,
                                            formatterFunc, columnOrderings)
                    query += ", "

            return query
        else:
            return ""


def __insertOneRow(one_entity, formatterFunc, columnOrderings):
    query = "("
    for ind, key in enumerate(columnOrderings):
        if ind == len(columnOrderings) - 1:
            query += formatterFunc(key, one_entity[key])
        else:
            query += formatterFunc(key, one_entity[key]) + ", "    
    query += ")"

    return query