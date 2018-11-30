<!-- Example : from https://gist.github.com/iros/3426278 -->

**Show Station Information**
----
  Returns JSON data about stations.

* **URL**

  `/station`

  `/station?parameter=[val]`
  
  `/station?parameter1=[val1]&parameter2=[val2]&...&parameterN=[valN]`

* **Method:**

  `GET` | `POST`
  
*  **URL Params**

   **Required:**
 
   No parameters are required.

   **Optional:**
 
   - `station_id=[integer]`,
   - `station_name=[alphanumeric]`,
   - `latitude=[double/float]`,
   - `longitude=[double/float]`,
   - `short_name=[alphanumeric]`,
   - `rental_methods=[stringone of 'CREDITCARD', 'KEY', 'BOTH']`,
   - `capacity=[integer]`,
   - `rental_id=[alphanumeric]`,
   - `eightd_has_key_dispenser=[boolean]`,
   - `has_kiosk=[boolean]`


* **Data Params**

  Only when making a POST request, pass a JSON that looks like:

  ```
  {
      "station" : {
          "station_id" : [integer],
          "station_name" : [alphanumeric],
          "latitude" : [double/float],
          "longitude" : [double/float],
          "short_name" : [alphanumeric],
          "rental_methods" : [one of 'CREDITCARD', 'KEY', 'BOTH'],
          "capacity" : [integer],
          "rental_id" : [alphanumeric],
          "eightd_has_key_dispenser" : [boolean],
          "has_kiosk" : [boolean]
      }
  }
  ```

  for inserting one station, or like:

  ```
  {
      "stations" : [
          {
              "station_id" : [integer],
              "station_name" : [alphanumeric],
              "latitude" : [double/float],
              "longitude" : [double/float],
              "short_name" : [alphanumeric],
              "rental_methods" : [one of 'CREDITCARD', 'KEY', 'BOTH'],
              "capacity" : [integer],
              "rental_id" : [alphanumeric],
              "eightd_has_key_dispenser" : [boolean],
              "has_kiosk" : [boolean]
          },
          ....
          {
              "station_id" : [integer],
              "station_name" : [alphanumeric],
              "latitude" : [double/float],
              "longitude" : [double/float],
              "short_name" : [alphanumeric],
              "rental_methods" : [one of 'CREDITCARD', 'KEY', 'BOTH'],
              "capacity" : [integer],
              "rental_id" : [alphanumeric],
              "eightd_has_key_dispenser" : [boolean],
              "has_kiosk" : [boolean]
          }
      ]
  }
  ```

for multiple stations.

* **Success Response:**
  
  <_What should the status code be on success and is there any returned data? This is useful when people need to to know what their callbacks should expect!_>

  * **Code:** 200 <br />
    **Content:** `{ stations : [...]  }` <br />
    **Description** A JSON aray of station data
 
@TODO - Error Responses, Sample Call, Notes

*  **Error Response:**

  <!--<_Most endpoints will have many ways they can fail. From unauthorized access, to wrongful parameters etc. All of those should be liste d here. It might seem repetitive, but it helps prevent assumptions from being made where they should be._>

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "Log in" }`

  OR

* **Code:** 422 UNPROCESSABLE ENTRY <br />
    **Content:** `{ error : "Unknown Parameter Provided: [the param and value provided]" }`

  OR
  
* **Code:** 422 UNPROCESSABLE ENTRY <br />
  **Content:** `{ error : "Station already exists - Operation Aborted: [the station that failed]" }` -->
    


*   **Sample Call:**

  <!--<_Just a sample call to your endpoint in a runnable format ($.ajax call or a curl request) - this makes life easier and more predictable._> -->

*   **Notes:**

  <!--<_This is where all uncertainties, commentary, discussion etc. can go. I recommend timestamping and identifying oneself when leaving comments here._> -->