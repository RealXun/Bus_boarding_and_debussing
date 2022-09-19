# Bus boarding and debussing

![](https://github.com/RealXun/Bus_boarding_and_debussing/blob/main/Resources/Bus%20In%20Out.png)

This bus has a passenger boarding and alighting control system to monitor the number of occupants it carries and thus detect when the capacity is too high.

At each stop the boarding and alighting of passengers is represented by a tuple composed of two integers.
```
bus_stop = (in, out)
```
The sequence of stops is represented by a list of these tuples.
```
stops = [(in1, out1), (in2, out2), (in3, out3), (in4, out4)]
```

## Objectives:
* lists, tuples
* while/for loops
* min, max, length
* mean, standard deviation

## Chores
1. Calculate the number of stops.
2. Assign to a variable a list whose elements are the number of passengers at each stop (in-out),
3. Find the maximum occupancy of the bus.
4. Calculate the mean occupancy. And the standard deviation.

### Solution
```
stops = [(10, 0), (4, 1), (3, 5), (3, 4), (5, 1), (1, 5), (5, 8), (4, 6), (2, 3)]
movement = []
occupation = []
total_stops=len(stops)
for up,down in stops:
    movement.append(up - down)
    print(movement)
for i in range(total_stops):
    occupation.append(sum(movement[0:i+1]))
print("The maximum occupation in the bus is", max(occupation), "persons")
print("The average occupation is", round((sum(occupation)/total_stops), 2),"persons")
import statistics
print("The standard deviation of the occupation is", round(statistics.stdev(occupation), 2))
```
