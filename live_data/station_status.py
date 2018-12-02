import requests

station_status_url = "https://gbfs.bluebikes.com/gbfs/en/station_status.json"

def poll(incomplete_url, role):
    # new_station_status_id = get_last_station_status_id(incomplete_url, role) + 1
    
    station_statuses = get_station_statuses()
    insert_query = ("insert into station_status ( " + 
                    "station_status_id, " + 
                    "station_id, " + 
                    "num_bikes_available, " + 
                    "num_ebikes_available, " + 
                    "num_bikes_disabled, " + 
                    "num_docks_available, " + 
                    "num_dock_disabled, " + 
                    "is_installed, " + 
                    "is_rented, " + 
                    "is_returning, " + 
                    "last_reported, " + 
                    "eightd_has_available_keys) values ")

    for station_status in station_statuses:
        insert_query += ("(" +
                        str(new_station_status_id) + "," +
                        str(station_status["station_id"]) + "," +
                        str(station_status["num_bikes_available"]) + "," +
                        str(station_status["num_ebikes_available"]) + "," +
                        str(station_status["num_bikes_disabled"]) + "," +
                        str(station_status["num_docks_available"]) + "," +
                        str(station_status["num_docks_disabled"]) + "," +
                        str(station_status["is_installed"]) + "," +
                        str(station_status["is_renting"]) + "," +
                        str(station_status["is_returning"]) + "," +
                        str(station_status["last_reported"]) + "," +
                        str(station_status["eightd_has_available_keys"]) + "),\n")

    insert_query = insert_query[:-2] + ";" 

    with open("station_statuses.txt", "a") as f:
        # replace the last comma with a semicolon
        f.write(insert_query)

    # complete_get_id_url = incomplete_url + "/mutate/" + insert_query + "/" + role
    # return requests.get(complete_get_id_url)

def get_last_station_status_id(incomplete_url, role):
    get_id_query = "select station_status_id from station_status"
    complete_get_id_url = incomplete_url + "/query/" + get_id_query + "/" + role
    
    station_status_ids = requests.get(complete_get_id_url).json()["result"]
    
    if station_status_ids:
        n = len(station_status_ids)
        return station_status_ids[n-1]
    else:
        return 0

def get_station_statuses():
    return requests.get(station_status_url).json()["data"]["stations"]

poll_result = poll("http://localhost:8001", "data-creator")
print(poll_result)