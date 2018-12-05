import csv, json, requests
from collections import OrderedDict


api_svc_address = "http://localhost"
api_svc_port = "8001"
api_svc_endpoint = "/"

api_svc_url= api_svc_address + ":" + api_svc_port + api_svc_endpoint

def find_stations(csvfilepath):
    stations=requests.get(api_svc_url+"station/data-creator").json()["stations"]
    station_ids=[]
    for index, station in enumerate(stations):
        station_ids.append(stations[index]["station_id"])

    bad_ids=[]
    with open(csvfilepath) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            trip = dict(row)
            start_station_id=trip.pop("start station id")
            stop_station_id=trip.pop("end station id")

            if not (int(start_station_id) in station_ids):
                bad_ids.append(start_station_id)
            if not (int(stop_station_id) in station_ids):
                bad_ids.append(stop_station_id)
    bad_ids=list(OrderedDict.fromkeys(bad_ids))
    print(bad_ids)
    return bad_ids
    


                



find_stations("files/201810-bluebikes-tripdata.csv")