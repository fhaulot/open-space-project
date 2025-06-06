

# Import libraries needed to run the code
#from utils.openspace import Openspace
import random
import pandas as pd

# Request the user to indicate the path to the file with the attendants list
#path = input("Please specify the file patch with the list of attendants:")
path = "C:/Users/bljor/OneDrive/Documents/GitHub/colleagues.csv"

# Initiate a list to include all attendants in the file
attendants = []

# Read the file and save the attendants
with open(path, "r") as my_file:
    names = my_file.read().split(" ")
    attendants.append(names)

# Check the number of attendants input
print(attendants)
#seats = len(attendants)

# Summarise the input
# print(f"Thank you! Your file includes {seats} attendants.\n\nHere is the list:")
# print(*attendants, sep ='\n')

# Call the different methods that will set the class organisation
# Set all attendants to their seats
#Openspace.organize(attendants)

# Show the seating layout
#Openspace.display()

# Save the layout to Excel in active directory
#Openspace.store("seating_arrangement.xlsx")

