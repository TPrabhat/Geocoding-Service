# Geocoding-Service
This service resolves the latitude and longitude for that address by using geocoding service APIs of Google and HERE
HERE APIs are used as primary service and Google maps is the back up API service. If there are multiple matches all of them are displayed with HERE and only the best match is displayed with Google API.

## Requirements
* **Python 3**

## Using your APIs
Create a python file called config and fill in your HERE APIs as
MY_APP_ID = "your app id"
MY_APP_Code = "your app code"

## Using the Service

The class method GeoCode can be used to retrieve the coordinates of an address by passing the address as an argument

```
object.GeoCode("enter your address here")
```

The file demo.py has example lines of code


## Alternate way

You may also decode multiple addresses one at a time by using the Run classmethod

```
object.GeoCode.Run()
```
Using the above method will prompt user to enter the address and retrieve co ordinates continuously until the user types exit
