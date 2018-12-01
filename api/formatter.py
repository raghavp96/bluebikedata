import datetime


def formatStationAttributeValue(keyName, value):
    return str({
        "station_id": value,
        "station_name": ("'" + str(value) + "'"),
        "latitude": value,
        "longitude": value,
        "short_name": ("'" + str(value) + "'"),
        "rental_methods": ("'" + str(value) + "'"),
        "capacity": value,
        "rental_id": ("'" + str(value) + "'"),
        "eightd_has_key_dispenser": __convertBool(value),
        "has_kiosk": __convertBool(value)
    }[keyName])


def reverseformatStationAttributeValue(keyName, value):
    return str({
        "station_id": value,
        "station_name": value,
        "latitude": value,
        "longitude": value,
        "short_name": value,
        "rental_methods": value,
        "capacity": value,
        "rental_id": value,
        "eightd_has_key_dispenser": __revConvertBool(value),
        "has_kiosk": __revConvertBool(value)
    }[keyName])


def formatStationStatusAttributeValue(keyName, value):
    return str({
        "station_status_id": value,
        "station_id": value,
        "num_bikes_available": value,
        "num_ebikes_available": value,
        "num_bikes_disabled": value,
        "num_docks_available": value,
        "num_dock_disabled": value,
        "is_installed": __convertBool(value),
        "is_rented": __convertBool(value),
        "is_returning": __convertBool(value),
        "last_reported": __convertSecToTime(value),
        "eightd_has_available_keys": __convertBool(value)
    }[keyName])


def reverseFormatStationStatusAttributeValue(keyName, value):
    return str({
        "station_status_id": value,
        "station_id": value,
        "num_bikes_available": value,
        "num_ebikes_available": value,
        "num_bikes_disabled": value,
        "num_docks_available": value,
        "num_dock_disabled": value,
        "is_installed": __revConvertBool(value),
        "is_rented": __revConvertBool(value),
        "is_returning": __revConvertBool(value),
        "last_reported": value,
        "eightd_has_available_keys": __revConvertBool(value)
    }[keyName])


def formatTripAttributeValue(keyName, value):
    return str({
        "trip_id": value,
        "bike_id": value,
        "start_time": __convertSecToTime(value),
        "end_time": __convertSecToTime(value),
        "usertype": ("'" + str(value) + "'"),
        "birthyear": value,
        "gender": __convertGenderToId(value),
        "start_station": value,
        "stop_station": value
    }[keyName])


def reverseFormatTripAttributeValue(keyName, value):
    return str({
        "trip_id": value,
        "bike_id": value,
        "start_time": value,
        "end_time": value,
        "usertype": value,
        "birthyear": value,
        "gender": __revConvertGender(value),
        "start_station": value,
        "stop_station": value
    }[keyName])


def __convertBool(val):
    if val == "true" or "1":
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
