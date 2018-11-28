TODO - Make API RESTful - don't allow people to make SQL queries on the fly

Allowed requests from webapp:

GET /query/trip
    /query/trip?start_station=x&time=y ... filter options

GET /query/station
GET /station_status

Additional allowed requests from data service:

POST /query/trip/{data}
POST /query/station/{data}
POST /query/station_status/{}
