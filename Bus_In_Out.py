stops = [(10, 0), (4, 1), (3, 5), (3, 4), (5, 1), (1, 5), (5, 8), (4, 6), (2, 3)]
movement = []
occupation = []
# 1. Calculate the number of stops.
total_stops=len(stops)
# 2. Assign to a variable a list whose elements are the number of passengers in
# each stop: Each element depends on the previous element in the list + in - out.
for up,down in stops:
    movement.append(up - down)
    print(movement)
# 3. Find the maximum occupancy of the bus.
for i in range(total_stops):
    occupation.append(sum(movement[0:i+1]))
print("The maximum occupation in the bus is", max(occupation), "persons")
# 4. Calculate the average occupancy. And the standard deviation.
print("The average occupation is", round((sum(occupation)/total_stops), 2),"persons")
import statistics
print("The standard deviation of the occupation is", round(statistics.stdev(occupation), 2))