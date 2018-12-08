import requests

gbfs_station_url = "https://gbfs.bluebikes.com/gbfs/en/station_information.json"
api_svc_role = "data-creator"


def poll(api_svc_url):
    post_data = {}
    post_data["stations"] = __get_latest_station_information()

    current_station_infos = __get_current_station_info(api_svc_url)
    current_station_ids = [station["station_id"]
                           for station in current_station_infos if "station_id" in station]

    new_post_data = {}
    new_post_data["stations"] = []

    for station in post_data["stations"]:
        if int(station["station_id"]) not in current_station_ids:
            new_post_data["stations"].append(__transform(station))

    if new_post_data["stations"] == []:
        return "No new stations to insert!"
    else:
        result = requests.post(api_svc_url + "station/" +
                               api_svc_role + "/", json=new_post_data)
        return ("API Response Code: ", result.status_code, "\n",
                "API Response: ", result.text)


def __transform(station):
    temp = station
    temp["station_name"] = station["name"]
    temp["latitude"] = station["lat"]
    temp["longitude"] = station["lon"]
    temp["rental_id"] = station["rental_url"]

    if station["rental_methods"] == ["KEY"]:
        temp["rental_methods"] = "KEY"
    elif station["rental_methods"] == ["CREDITCARD"]:
        temp["rental_methods"] = "CREDITCARD"
    else:
        temp["rental_methods"] = "BOTH"

    return temp


def __get_current_station_info(api_svc_url):
    url = api_svc_url + "station"

    stations = requests.get(url).json()["stations"]
    return stations


def __get_latest_station_information():
    return requests.get(gbfs_station_url).json()["data"]["stations"]