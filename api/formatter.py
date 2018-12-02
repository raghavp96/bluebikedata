import datetime


def formatStationAttributeValue(keyName, value):
    if keyName in ["station_id", "latitude", "longitude", "capacity"]:
        return str(value)
    elif keyName in ["station_name", "short_name", "rental_methods", "rental_id"]:
        return ("'" + str(value) + "'")
    elif keyName in ["eightd_has_key_dispenser", "has_kiosk"]:
        return __convertBool(value)
    else:
        return str(value)


def reverseformatStationAttributeValue(keyName, value):
    if keyName in ["station_id", "latitude", "longitude", "capacity"]:
        return value
    elif keyName in ["station_name", "short_name", "rental_methods", "rental_id"]:
        return value
    elif keyName in ["eightd_has_key_dispenser", "has_kiosk"]:
        return __revConvertBool(value)
    else:
        return value


def formatStationStatusAttributeValue(keyName, value):
    if keyName in [
        "station_status_id", "station_id", "num_bikes_available", 
        "num_ebikes_available", "num_bikes_disabled", "num_docks_available", 
        "num_dock_disabled"]:
        return str(value)
    elif keyName in [
        "is_installed", "is_rented", "is_returning", 
        "eightd_has_available_keys"]:
        return __convertBool(value)
    elif keyName in ["last_reported"]:
        return __convertSecToTime(value)
    else:
        return str(value)


def reverseFormatStationStatusAttributeValue(keyName, value):
    if keyName in [
        "station_status_id", "station_id", "num_bikes_available", 
        "num_ebikes_available", "num_bikes_disabled", "num_docks_available", 
        "num_dock_disabled", "last_reported"]:
        return value
    elif keyName in [
        "is_installed", "is_rented", "is_returning", 
        "eightd_has_available_keys"]:
        return __revConvertBool(value)
    elif keyName in keyName in ["last_reported"]:
        return value
    else:
        return value


def formatTripAttributeValue(keyName, value):
    if keyName in [
        "trip_id", "bike_id", "birthyear", "start_station", 
        "stop_station"]:
        return str(value)
    elif keyName in ["start_time", "end_time"]:
        return __convertSecToTime(value)
    elif keyName in ["usertype"]:
        return ("'" + str(value) + "'")
    elif keyName in ["gender"]:
        __convertGenderToId(value)
    else:
        return str(value)


def reverseFormatTripAttributeValue(keyName, value):
    if keyName in [
        "trip_id", "bike_id", "birthyear", "start_station", 
        "stop_station"]:
        return value
    elif keyName in ["start_time", "end_time"]:
        return value
    elif keyName in ["usertype"]:
        return value
    elif keyName in ["gender"]:
        return __revConvertGender(value)
    else:
        return value


def __convertBool(val):
    if val == "true" or val == 1 or val == True:
        return "TRUE"
    else:
        return "FALSE"


def __convertGenderToId(val):
    if val == "F":
        return 1
    else:
        return 2


def __convertSecToTime(val):
    return "'" + datetime.datetime.fromtimestamp(val).strftime("%Y-%m-%d %H:%M:%S") + "'"


def __revRemoveSingleQuotes(val):
    if val.startswith("'") and val.endswith("'"):
        val = val[1:-1]
    return val


def __revConvertBool(val):
    if val == 1 or val == "TRUE":
        return "true"
    elif val == 0 or val == "FALSE":
        return "false"
    else:
        return val


def __revConvertGender(val):
    if val == 1:
        return "M"
    elif val == 2:
        return "F"
    else:
        return "U"