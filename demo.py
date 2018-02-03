# import the module
from GeoCoder import GeoCoder

# create an object and instantiate the class
g = GeoCoder()

# Prompt user to enter address
address = input("Enter the Address:\n")

# displays the co ordinates of the passed address
g.GeoCode(address)

# uncomment below to run multiple requests. type exit to finish execution
#g.Run()