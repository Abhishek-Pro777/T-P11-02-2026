total_no_of_wheels = int(input())
total_no_of_vehicles = int(input())
no_of_bikes = (4 * total_no_of_vehicles - total_no_of_wheels) // 2
no_of_cars = total_no_of_vehicles - no_of_bikes
print(no_of_bikes)
print(no_of_cars)
