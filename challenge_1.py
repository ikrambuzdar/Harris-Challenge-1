# CHALLENGE PROBLEMS
# YOU MAY NOT USE ANY ADDITIONAL LIBRARIES OR PACKAGES TO COMPLETE THIS CHALLENGE

# Divvy is Chicago's bike share system, which consists of almost 600 stations scattered
# around the city with blue bikes available for anyone to rent. Users begin a ride by removing
# a bike from a dock, and then they can end their ride by returning the bike to a dock at any Divvy 
# station in the city. You are going to use real data from Divvy collected at 1:30pm on 4/7/2020 
# to analyze supply and demand for bikes in the system. 

# NOTE ** if you aren't able to run this, type "pip install json" into your command line
import json

# do not delete; this is the data you'll be working with
divvy_stations = json.loads(open('divvy_stations.txt').read())

# PROBLEM 1
# find average number of empty docks (num_docks_available) and 
# available bikes (num_bikes_available) at all stations in the system
empty_docks = [d['num_docks_available'] for d in divvy_stations]
avg_emptydocks = sum(empty_docks)/len(empty_docks)
print(avg_emptydocks)  #answer is 9.532773109243697

available_bikes = sum([a['num_bikes_available'] for a in divvy_stations])
print(available_bikes)   # answer is 4617



# PROBLEM 2
# find ratio of bikes that are currently rented to total bikes in the system (ignore ebikes)

rented = sum([r['is_renting'] for r in divvy_stations])
rent_ratio = rented/(rented+available_bikes)    #     rented = 595, total = 5212  
rent_ratio   #ratio = 0.114

# PROBLEM 3 
# Add a new variable for each divvy station's entry, "percent_bikes_remaining", that shows 
# the percentage of bikes available at each individual station (again ignore ebikes). 
# This variable should be formatted as a percentage rounded to 2 decimal places, e.g. 66.67%
number_bikes_availabl = [a['num_bikes_available'] for a in divvy_stations]
num_docks_available = [d['num_docks_available'] for d in divvy_stations]
total_bikes_spaces =[number_bikes_availabl[i] + num_docks_available[i] for i in range(len(number_bikes_availabl))]
percent_bikes_remaining = [str(number_bikes_availabl[i]/total_bikes_spaces[i])[:4] + '%' for i in range(len(number_bikes_availabl))]
percent_bikes_remaining
new_divvy_list = [dict(divvy_old_data, percent_bikes_remaining = a) for divvy_old_data, a in zip(divvy_stations, percent_bikes_remaining)]
new_divvy_list
