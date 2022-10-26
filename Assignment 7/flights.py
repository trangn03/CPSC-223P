# Name: Trang Ngo
# Date: 10/26/2022
# File Purpose: Contains a list of flight schedule data

import json
import datetime

class Flights:
    def __init__(self,filename):
        # Set member variable equal to the filename
        self.filename = filename
        # Set member variable equal to an empty data list
        self.data = []
        # Open the filename and load the JSON decoded contents to the empty data list
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        # Cleanly manage the FileNotFoundError if the filename does not exist.
        except FileNotFoundError:
                pass
    
    # Write the JSON encode contents of the member variable data list to the filename
    # that was set to the member variable
    def write_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)
    
    def add_flight(self,origin,destination,flight_num,departure,next_day,arrival):
        # if either the departure or arrival string is not in the proper format
        # return False
        if len(departure) != 4 or departure.isnumeric() is False:
            return False
        elif len(arrival) != 4 or arrival.isnumeric() is False:
            return False
        # Append the data to the member variable data list
        else:
            self.data.append([origin,destination,flight_num,departure,next_day,arrival])
            # JSON encode contents
            self.write_data()
            return True

    def get_flights(self):
        # Flight schedule data
        flight_schedule = []
        for x in self.data:
            origin = x[0]
            destination = x[1]
            flight_num = x[2]
            departure_hour = x[3][:2]
            departure_min = x[3][2:]
            next_day = x[4]
            arrival_hour = x[5][:2]
            arrival_min = x[5][2:]

            departure = datetime.datetime(1,1,1,int(departure_hour),int(departure_min),0)
            # return a string representing date and time
            departure_str = departure.strftime("%I").lstrip("0") + ":" + departure.strftime("%M") + departure.strftime("%p").lower()
            arrival = datetime.datetime(1,1,1,int(arrival_hour),int(arrival_min),0)
            arrival_str = arrival.strftime("%I").lstrip("0") + ":" + arrival.strftime("%M") + arrival.strftime("%p").lower()
            
            if next_day == "Y":
                arrival = datetime.datetime(1,1,2,int(arrival_hour),int(arrival_min),0)
                arrival_str = "+" + arrival.strftime("%I").lstrip("0") + ":" + arrival.strftime("%M") + arrival.strftime("%p").lower()
            
            delta = arrival - departure
            second = delta.seconds
            hours = second // 3600
            second %= 3600
            minutes = second // 60
            duration_str = f'{hours}:{minutes:02}'
            
            flight_schedule.append([origin,destination,flight_num,departure_str,arrival_str,duration_str])
            return flight_schedule