import csv, json, requests

api_svc_url = "http://api_svc:8080/"
test_api_svc_url = "http://localhost:8001/"

def default_convert_csv_to_json(csvfilepath):
    post_data = {"trips":[]}
    tripsToIgnore = []
    with open(csvfilepath) as csv_file:
        fieldnames = ("tripduration","start_time","end_time","start_station","start_station_name",
        "start_station_latitude","start_station_longitude","stop_station","end_station_name",
        "end_station_latitude","end_station_longitude","bike_id","usertype","birthyear","gender")

        irrelevantColumns = ["tripduration", "start_station_name", "start_station_latitude", "start_station_longitude",
        "end_station_name", "end_station_latitude","end_station_longitude"]

        numberColumns = ["start_station","stop_station","bike_id","birthyear","gender"]
        dateColumns = ["start_time","end_time"]
        
        reader = csv.DictReader(csv_file, fieldnames)
        latest_trip_id=requests.get(api_svc_url+"trip_latest_id").json()["latest_trip_id"]
        for row in reader:
            trip = dict(row)
            # removes irrelevant columns
            for column in irrelevantColumns:
                trip.pop(column, None)

            post_data["trips"].append(trip)

        post_data.get("trips").pop(0)

        for indx, trip in enumerate(post_data["trips"]):
            # Add the trip id to the JSON
            latest_trip_id=latest_trip_id+1

            for key in trip.keys():
                if trip[key] is None:
                    tripsToIgnore.append(indx)
                else:  
                    if key in numberColumns:
                        trip[key] = int(trip[key])
                    elif key in dateColumns:
                        trip[key] = trip[key].split(".")[0]
                    else:
                        trip[key] = trip[key]
            
            trip["trip_id"] = latest_trip_id
    
    for tripIndex in tripsToIgnore:
        post_data.get("trips").pop(tripIndex, None)

    # # return post_data
    result = requests.post(api_svc_url + "trip/data-creator/", json=post_data)
    response = {
        "API Response Code: " : result.status_code,
        "API Response: " : result.text
    } 
    return response