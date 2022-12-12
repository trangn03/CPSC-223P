# Name: Trang Ngo
# Date: 10/26/2022
# File Purpose: Output and call all of the functions

import flights
f = flights.Flights('f.dat')
while True:
    print("      *** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU")
    print()
    print("1. Add flight")
    print("2. Print flight schedule")
    print("3. Set flight schedule filename")
    print("9. Exit the program")
    print()
    # Enter user choice
    choice = int(input("Enter menu choice: "))
    print()

    if choice == 1:
        origin = input("Enter origin: ")
        destination = input("Enter destination: ")
        flight_num = input("Enter flight number: ")
        departure = input("Enter departure time (HHMM): ")
        arrival = input("Enter arrival time (HHMM): ")
        next_day = input("Is arrival next day (Y/N): ")

        f.add_flight(origin,destination,flight_num,departure,arrival,next_day)
        print()

    elif choice == 2:
        flight = f.get_flights()
        print("================== FLIGHT SCHEDULE ==================")
        print("Origin Destination Number Departure  Arrival Duration")
        print("====== =========== ====== ========= ======== ========")
        for x in flight:
            origin = x[0]
            destination = x[1]
            flight_num = x[2]
            departure = x[3]
            arrival = x[4]
            duration = x[5]
            print(f'{origin:7}{destination:12}{flight_num:>6}{departure:>10}{arrival:>9}{duration:>9}')
            print()

    elif choice == 3:
        file_name = input("Enter filename: ")
        f = flights.Flights(file_name)
        print()

    elif choice == 9:
        break
    else:
        print("Invalid choice")