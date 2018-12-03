import requests

station_url = "https://gbfs.bluebikes.com/gbfs/en/station_information.json"

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

    post_data = {}
    post_data["stations"] = get_station_information()

    print(post_data)

    for station in post_data["stations"]:
        station = transform(station)
  
    return requests.post(api_svc_url + "station/data-creator/", json=post_data)

def transform(station):
    temp = station
    temp["station_name"] = station["name"]
    temp["latitude"] = station["lat"]
    temp["longitude"] = station["lon"]
    temp["rental_id"]  = station["rental_url"]

    if station["rental_methods"] == ["KEY"]:
        temp["rental_methods"] = "KEY"
    elif station["rental_methods"] == ["CREDITCARD"]:
        temp["rental_methods"] = "CREDITCARD"
    else:
        temp["rental_methods"] = "BOTH"

    return temp

def get_stations():
    url = api_svc_url + "station"

    stations = requests.get(url).json()["stations"]
    return stations

def get_station_information():
    return requests.get(station_url).json()["data"]["stations"]

poll_result = poll()
print(poll_result.text)