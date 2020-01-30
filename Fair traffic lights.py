north_int = int(input("Number of cars travelling north: "))
south_int = int(input("Number of cars travelling south: "))
east_int = int(input("Number of cars travelling east: "))
west_int = int(input("Number of cars travelling west: "))

sum_of_cars = north_int + south_int + east_int + west_int

n/s = 0
e/w = 0

while sum_of_cars > 0:
    if n/s > e/w:
        print("Green light on N/S")
    else:

"""
while ((north_int or south_int) > (east_int or west_int)):
    print("Green light on N/S")


print("Green light on E/W")
print("No cars waiting, the traffic jam has been solved!")