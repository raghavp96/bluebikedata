import csv, json, requests
from collections import OrderedDict


def find_stations(csvfilepath, url):
    stations=requests.get(url + "station").json()["stations"]
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

            if int(start_station_id) not in station_ids:
                bad_ids.append(int(start_station_id))
            if int(stop_station_id) not in station_ids:
                bad_ids.append(int(stop_station_id))
    bad_ids=list(OrderedDict.fromkeys(bad_ids))
    print(bad_ids)
    return bad_ids
