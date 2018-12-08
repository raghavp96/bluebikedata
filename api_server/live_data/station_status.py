import requests

gbfs_station_status_url = "https://gbfs.bluebikes.com/gbfs/en/station_status.json"
api_svc_role = "data-creator"


def poll(api_svc_url):
    new_station_status_id = __get_last_station_status_id(api_svc_url)

    post_data = {}
    post_data["station_statuses"] = __get_station_statuses()

    for item in post_data["station_statuses"]:
        item["station_status_id"] = new_station_status_id + 1
        item["num_dock_disabled"] = item["num_docks_disabled"]
        item["is_rented"] = item["is_renting"]

    result = requests.post(api_svc_url + "station_status/" +
                           api_svc_role + "/", json=post_data)
    return ("API Response Code: ", result.status_code, "\n",
            "API Response: ", result.text)


def __get_last_station_status_id(api_svc_url):
    url = api_svc_url + "station_status/latest_id"
    latest_station_status_id = requests.get(
        url).json()["latest_station_status_id"]

    return latest_station_status_id


def __get_station_statuses():
    return requests.get(gbfs_station_status_url).json()["data"]["stations"]