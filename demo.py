# import the module
from GeoCoder import GeoCoder

# create an object and instantiate the class
g = GeoCoder()

while True:
    # Prompt user to enter address
    address = input("Enter the Address:\n")

    if address == 'exit':
        print("Thank you")
        break

    # displays the co ordinates of the passed address
    g.GeoCode(address)