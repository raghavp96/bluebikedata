**Show Station Status Information**
----
  Returns JSON data about the statuses of stations.

* **URL**

  `/station_status`

  `station_status/latest`

  `/station_status?parameter=[val]`
  
  `/station_status?parameter1=[val1]&parameter2=[val2]&...&parameterN=[valN]`

* **Method:**

  `GET` | `POST`
  
*  **URL Params**

   **Required:**
 
   No parameters are required.

   **Optional:**

    - `station_status_id=[integer]`, (the larger this number, the more recent the status information set)
    - `station_id=[integer]`, (realistically the only useful parameter to search by, as others can change rapidly)
    - `num_bikes_available=[integer],`
    - `num_ebikes_available=[integer]`,
    - `num_bikes_disabled=[integer]`,
    - `num_docks_available=[integer]`,
    - `num_dock_disabled=[integer]`,
    - `is_installed=[boolean]`,
    - `is_rented=[boolean]`,
    - `is_returning=[boolean]`,
    <!-- (- `last_reported datetime=[long integer]`,)-->
    - `eightd_has_available_keys=[boolean]`

* **Data Params**

  Only when making a POST request, pass a JSON that looks like:

  ```
  {
      "station_status" : {
          "station_status_id"  : [integer],
          "station_id"  : [integer],
          "num_bikes_available"  : [integer],
          "num_ebikes_available"  : [integer],
          "num_bikes_disabled"  : [integer],
          "num_docks_available"  : [integer],
          "num_dock_disabled"  : [integer],
          "is_installed"  : [boolean],
          "is_rented"  : [boolean],
          "is_returning"  : [boolean],
          "last_reported" [long integer],
          "eightd_has_available_keys"  : [boolean]
      }
  }
  ```

  for creating the status for station, or like:

  ```
  {
      "station_statuses" : [
          {
              "station_status_id"  : [integer],
              "station_id"  : [integer],
              "num_bikes_available"  : [integer],
              "num_ebikes_available"  : [integer],
              "num_bikes_disabled"  : [integer],
              "num_docks_available"  : [integer],
              "num_dock_disabled"  : [integer],
              "is_installed"  : [boolean],
              "is_rented"  : [boolean],
              "is_returning"  : [boolean],
              "last_reported" [long integer],"eightd_has_available_keys"  : [boolean]
          },
          ...
          {
              "station_status_id"  : [integer],
              "station_id"  : [integer],
              "num_bikes_available"  : [integer],
              "num_ebikes_available"  : [integer],
              "num_bikes_disabled"  : [integer],
              "num_docks_available"  : [integer],
              "num_dock_disabled"  : [integer],
              "is_installed"  : [boolean],
              "is_rented"  : [boolean],
              "is_returning"  : [boolean],
              "last_reported" [long integer],"eightd_has_available_keys"  : [boolean]
          }
      ]
  }
  ```

for the status data for multiple stations.


* **Success Response:**
  
  <_What should the status code be on success and is there any returned data? This is useful when people need to to know what their callbacks should expect!_>

  * **Code:** 200 <br />
    **Content:** `{ station_statuses : [...] }`
 
@TODO - Error Responses, Sample Call, Notes

* **Error Response:**
<!--
  <_Most endpoints will have many ways they can fail. From unauthorized access, to wrongful parameters etc. All of those should be liste d here. It might seem repetitive, but it helps prevent assumptions from being made where they should be._>

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "Log in" }`

  OR

  * **Code:** 422 UNPROCESSABLE ENTRY <br />
    **Content:** `{ error : "Email Invalid" }` -->

* **Sample Call:**

<!-- <_Just a sample call to your endpoint in a runnable format ($.ajax call or a curl request) - this makes life easier and more predictable._>  -->

* **Notes:**

 <!-- <_This is where all uncertainties, commentary, discussion etc. can go. I recommend timestamping and identifying oneself when leaving comments here._>  -->

----

 **Show the Last Station Status ID**
----
  Returns JSON data containing the last used id for station_status.

* **URL**

  `/station_status/latest_id`

* **Method:**

  `GET`
  
*  **URL Params**
 
   No parameters necessary .

* **Success Response:**
  
  <_What should the status code be on success and is there any returned data? This is useful when people need to to know what their callbacks should expect!_>

  * **Code:** 200 <br />
    **Content:** `{ "latest_station_status_id" : [a number] }`
 
@TODO - Error Responses, Sample Call, Notes

* **Error Response:**


* **Sample Call:**

```
curl "http://localhost:8001/station_status/latest_id
```

* **Notes:**

 <!-- <_This is where all uncertainties, commentary, discussion etc. can go. I recommend timestamping and identifying oneself when leaving comments here._>  -->

 