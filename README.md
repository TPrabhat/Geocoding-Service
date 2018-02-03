# Geocoding-Service
This service resolves the latitude and longitude for that address by using geocoding service APIs of Google and HERE
HERE APIs are used as primary service and Google maps is the back up API service. If there are multiple matches all of them are displayed with HERE and only the best match is displayed with Google API.

## Requirements
* **Python 3**

## Using your APIs
Create a python file called config and fill in your HERE APIs as__

MY_APP_ID = "your app id"__
MY_APP_Code = "your app code"

## Using the Service

From the command line type

```
python demo.py
```
The above will prompt user to enter an address. Once an address is input the matching co ordinates are displayed and the user is prompted to enter another address.
Type exit to terminate the program


## Using GeoCoder library

Use the class method GeoCode with the address passed as an argument to decode the co ordinates

### Example
GeoCoder.GeoCode("your address here")

## Sample input 1
```
Enter the Address:
955 Escalon Avenue
```

## Output 1
```
Using Geocoding service by HERE...
No. of matches found:  1

Match 1 of 1
Latitude:  20.7462433
Longitude:  -103.3537606
```

## Sample input 2
```
Enter the Address:
Sunnyvale
```

## Output 2
```
Using Geocoding service by HERE...
No. of matches found:  3

Match 1 of 3
Latitude:  37.37172
Longitude:  -122.03801

Match 2 of 3
Latitude:  32.78034
Longitude:  -96.54741

Match 3 of 3
Latitude:  -34.1769
Longitude:  137.84631
```
