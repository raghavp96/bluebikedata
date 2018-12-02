def intoSQL(trips):
    insert_query = ("insert into trip ( " + 
                    "trip_id, " + 
                    "bike_id, " + 
                    "start_time, " + 
                    "end_time, " + 
                    "usertype, " + 
                    "birthyear, " + 
                    "gender, " + 
                    "start_station, " + 
                    "stop_station) values ")
    for trip in trips["trips"]:
        insert_query += ("(" +
                        str("123") + "," +
                        str(trip["bikeid"]) + "," +
                        str(trip["starttime"]) + "," +
                        str(trip["stoptime"]) + "," +
                        str(trip["usertype"]) + "," +
                        str(trip["birthyear"]) + "," +
                        str(trip["gender"]) + "," +
                        str(trip["start_station_id"]) + "," +
                        str(trip["end_station_id"]) + ")")

    
    with open("trip_data.txt", "a") as f:
        f.write(insert_query)
    #complete_get_id_url = incomplete_url + "/mutate/" + insert_query + "/" + role
    #return requests.get(complete_get_id_url)