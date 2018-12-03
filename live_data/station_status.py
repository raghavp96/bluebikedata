import requests

station_status_url = "https://gbfs.bluebikes.com/gbfs/en/station_status.json"

# Don't hardcode
# api_svc_address = "http://api_svc"
# api_svc_port = "8080"
# api_svc_endpoint = "/"

# For local testing run make start - stop this container only
# Uncomment the following details and comment the above:

api_svc_address = "http://localhost"
api_svc_port = "8001"
api_svc_endpoint = "/"

api_svc_url= api_svc_address + ":" + api_svc_port + api_svc_endpoint

def poll():
    new_station_status_id = get_last_station_status_id()

    post_data = {}
    post_data["station_statuses"] = get_station_statuses()

    for item in post_data["station_statuses"]:
        item["station_status_id"] = new_station_status_id + 1
        item["num_dock_disabled"] = item["num_docks_disabled"]
        item["is_rented"] = item["is_renting"]
  
    return requests.post(api_svc_url + "station_status/data-creator/", json=post_data)

def get_last_station_status_id():
    url = api_svc_url + "station_status/latest"

    latest_station_status_set = requests.get(url).json()["station_statuses"]

    if latest_station_status_set == []:
        return 0
    else:
        return latest_station_status_set[0]["station_status_id"]

def get_station_statuses():
    return requests.get(station_status_url).json()["data"]["stations"]

poll_result = poll()
print(poll_result.text)