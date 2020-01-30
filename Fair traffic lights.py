north_int = int(input("Number of cars travelling north: "))
south_int = int(input("Number of cars travelling south: "))
east_int = int(input("Number of cars travelling east: "))
west_int = int(input("Number of cars travelling west: "))

sum_of_all_cars = north_int + south_int + east_int + west_int

while sum_of_all_cars > 0:
    north_and_south_sum = north_int + south_int
    east_and_west_sum = east_int + west_int

    north_counter = north_int
    south_counter = south_int
    east_counter = east_int
    west_counter = west_int

    north_and_south_sum = north_counter + south_counter
    east_and_west_sum = east_counter + west_counter
    if north_and_south_sum > east_and_west_sum:
        print("Green light on N/S")
        if north_counter >= 5:
            north_counter -= 5
            if sum_of_all_cars >= 5:
                sum_of_all_cars -= 5
            else:
                sum_of_all_cars = 0
        else:
            north_counter = 0
            
        if south_counter >= 5:
            south_counter -= 5
            if sum_of_all_cars >= 5:
                sum_of_all_cars -= 5
            else:
                sum_of_all_cars = 0
        else:
            south_counter = 0

    elif east_and_west_sum > north_and_south_sum:
        print("Green light on E/W")
        if east_counter >= 5:
            east_counter -= 5
            if sum_of_all_cars >= 5:
                sum_of_all_cars -= 5
            else:
                sum_of_all_cars = 0
        else:
            east_counter = 0
            
        if west_counter >= 5:
            west_counter -= 5
            if sum_of_all_cars >= 5:
                sum_of_all_cars -= 5
            else:
                sum_of_all_cars = 0
        else:
            west_counter = 0

print("No cars waiting, the traffic jam has been solved!")