# The API service

## Overview

The API consists of all the code in the `/api/` folder and will run in its own container when you call `make start` from the root directory.

The API, as a service, exposes certain behaviors for other entities (users or services) to make use of.

## The Interface: 

**Show Station Information**
----
  Returns JSON data about stations.

* **URL**

  `/station`

  `/station?parameter=[val]`
  
  `/station?parameter1=[val1]&parameter2=[val2]&...&parameterN=[valN]`

See `docs/api/methods/station.md` for full information.

----

**Show Station Status Information**
----
  Returns JSON data about the statuses of stations.

* **URL**

  `/station_status`

  `station_status/latest`

  `/station_status?parameter=[val]`
  
  `/station_status?parameter1=[val1]&parameter2=[val2]&...&parameterN=[valN]`

See `docs/api/methods/station_status.md` for full information.

----

**Show Trip Information**
----
  Returns JSON data about trips.

* **URL**

  `/trip`

  `/trip?parameter=[val]`
  
  `/trip?parameter1=[val1]&parameter2=[val2]&...&parameterN=[valN]`

See `docs/api/methods/trip.md` for full information.