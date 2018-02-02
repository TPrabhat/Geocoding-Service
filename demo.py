# import the module
from GeoCode import GeoCode

# create an object and instantiate the class
g = GeoCode()

# Prompt user to enter address
address = input("Enter the Address:\n")

# displays the co ordinates of teh passed address
g.GeoCode(address)

# uncomment below to run multiple requests. type exit to finish execution
#g.Run()