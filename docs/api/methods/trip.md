<!-- Example : from https://gist.github.com/iros/3426278 -->

**Show Trip Information**
----
  Returns JSON data about trips.

* **URL**

  `/trip`

  `/trip?parameter=[val]`
  
  `/trip?parameter1=[val1]&parameter2=[val2]&...&parameterN=[valN]`

* **Method:**

  `GET` | `POST`
  
*  **URL Params**

   **Required:**
 
   No parameters are required.

   **Optional:**
 
	- `trip_id=[integer]`,
    - `bike_id=[integer]`,
    - `start_time=[long integer]`,
    - `end_time=[long integer]`,
    - `usertype=[alphanumeric, one of ('Customer', 'Subscriber')]`,
    - `birthyear=[integer]`,
    - `gender=[boolean]`,
    - `start_station=[integer]`,
    - `stop_station=[integer]`


* **Data Params**

  Only when making a POST request, pass a JSON that looks like:

  ```
  {
      "trip" : {
          "trip_id" : [integer],
          "bike_id" : [integer],
          "start_time" : [long integer],
          "end_time" : [long integer],
          "usertype" : [alphanumeric],
          "birthyear" : [integer],
          "gender" : [boolean],
          "start_station" : [integer],
          "stop_station" : [integer]
      }
  }
  ```

  for inserting one station, or like:

  ```
  {
      "trips" : [
          {
              "trip_id" : [integer],
              "bike_id" : [integer],
              "start_time" : [long integer],
              "end_time" : [long integer],
              "usertype" : [alphanumeric],
              "birthyear" : [integer],
              "gender" : [boolean],
              "start_station" : [integer],
              "stop_station" : [integer]
          },
          ...
          {
              "trip_id" : [integer],
              "bike_id" : [integer],
              "start_time" : [long integer],
              "end_time" : [long integer],
              "usertype" : [alphanumeric],
              "birthyear" : [integer],
              "gender" : [boolean],
              "start_station" : [integer],
              "stop_station" : [integer]
          }
      ]
  }
  ```

for multiple stations.

* **Success Response:**
  
  <_What should the status code be on success and is there any returned data? This is useful when people need to to know what their callbacks should expect!_>

  * **Code:** 200 <br />
    **Content:** `{ trips : [...]  }` <br />
    **Description** A JSON aray of trip data
 
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