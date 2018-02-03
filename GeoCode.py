# import teh module to generate the request
import requests
import config

# define class
class GeoCode:

    # define the primary and secondary apis that will be used
    # variables below are class variables
    primary_api = "https://geocoder.api.here.com/6.2/geocode.json"
    secondary_api = "https://maps.googleapis.com/maps/api/geocode/json"

    # below are the parameters required to use the "here" api
    APP_ID = config.MY_APP_ID
    APP_Code = config.MY_APP_Code

    def __init__(self):
        pass


    # define primary api function
    def primary_geocoding_api(self, address):

        # define a dictionary to pass parameters
        PARAMS = {'app_id': self.APP_ID, 'app_code': self.APP_Code, 'searchtext': address}

        # send get request and saving the response as response object
        r = requests.get(url=self.primary_api, params=PARAMS)

        data = r.json()

        # provide a status update

        print("\nUsing Geocoding service by HERE...")

        # find the number of results found by the API
        num_matches = len(data['Response']['View'][0]['Result'])

        # display number of matches
        print("No. of matches found: ", num_matches, "\n")

        # iterate through all the addresses found and display thie co ordinates
        for i in range(0, num_matches):
            print("Match", i + 1, "of", num_matches)

            # extract latitude, longitude of the first matching location and print them
            print("Latitude: ", data['Response']['View'][0]['Result'][i]['Location']['DisplayPosition']['Latitude'])
            print("Longitude: ", data['Response']['View'][0]['Result'][i]['Location']['DisplayPosition']['Longitude'], "\n")


    # define secondary api function
    def secondary_geocoding_api(self, address):

        # define a dictionary to pass parameters
        PARAMS = {'address': address}

        # send get request and saving the response as response object
        r = requests.get(url=self.secondary_api, params=PARAMS)

        # extract data in json format
        data = r.json()

        # determine data status
        data_status = data['status']

        # provide a status update
        print("Using Geocoding service by Google...")

        if data_status == "OK":

            # extract latitude, longitude of the first matching location and print them
            print("Latitude: ", data['results'][0]['geometry']['location']['lat'])
            print("Longitude: ", data['results'][0]['geometry']['location']['lng'])
        else:
            print("Failed")
            raise Exception


    # Define the geocode method where primary and secondary apis are tried
    def GeoCode(self, address):

        self.address = address

        # only proceed if an address is entered
        if self.address:
            # Try to execute geocode using primary api
            try:

                self.primary_geocoding_api(self.address)

            # In case primary api fails to execute try geocode using secondary api
            except IndexError:
                print("Failed")
                try:

                    self.secondary_geocoding_api(self.address)

                # If secondary api also fails
                except Exception:

                    print("Sorry, No Results found for your address")

    def Run(self):

        while True:

            self.address = input("Enter the Address:\n")

            if self.address == 'exit':
                print("Thank you")
                break

            self.GeoCode(self.address)